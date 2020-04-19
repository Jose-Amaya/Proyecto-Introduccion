# This program runs non-stop updating and downloading the data when necessary

import os

deployed = os.name == 'posix'

if deployed:
    path = "/home/pi/project/data/files/" ## Informacion despacho nacional
else:
    path = os.getcwd() + "\\2. Programación\\project\\data\\files\\" ## Informacion despacho nacional

import dataTranslate as dt

import time
import datetime
import array
import json

import logging
logging.basicConfig(filename='dataUpdater.log',level=logging.DEBUG, format='%(asctime)s %(message)s')

global Centrales, cHour, cDay

retryWait = 30 # Seconds to wait to retry again after error

def getCent():
    parsedData = dt.parseData() # Download and parse data

    while not parsedData[0]: # If first argument is false there was an an error
        logging.error(str(parsedData[1])) # The second argument has the error, so we log it
        print(str(parsedData[1]))
        time.sleep(retryWait)
        parsedData = dt.parseData() # We wait and then try to get the data again

    return(parsedData[1]) # If there's no error, the second argument has the Central objects

def exportMatrixBin(): # As binary file
    mat = array.array('B')
    lights = [0]*56 # We waste some space, but the space is small and it's easier to write the data
    
    for i in range(0, len(Centrales)):
        lights[i] = 0 if Centrales[i].get(cHour) == 0 else 1 # we need the number to be 0 or 1, not a boolean value
    
    mat.fromlist(lights)

    file = open(path + "matSdata.bin", 'wb')
    mat.tofile(file)
    file.close()

def exportMatrix():
    lights = [0]*64

    for i in range(0, len(Centrales)):
        lights[i] = 0 if Centrales[i].get(cHour) == 0 else 1
    
    mat = [[lights[x+y*8] for x in range(0, 8)] for y in range(0,8)] # "flatten" the array

    file = open(path + "matSdata.txt", 'w')
    file.write(str(mat))
    file.close()

def exportJson():
    jsonData = open(path + "data.json", 'w')
    
    jsonCentrales = {}
    for i in Centrales:
        jsonCentrales.update({i.id:vars(i)});

    jsonCentrales.update({"time":str(datetime.datetime.today())}) # Save time of update (if there are errors the file will have the last time updated)
    # We show the errors in the webpage (which this file is made for), so showing the time on it is useful
    # A way to check for errors and show them on the webpage is to read the log file (comparing updated time (json) to error time (log) to know if the error is already fixed)

    json.dump(jsonCentrales, jsonData, indent=2)
    jsonData.close()

def updateToHour():
    global cHour
    cHour = datetime.datetime.today().hour

    #exportMatrix() # for matS.py
    exportMatrixBin() # for matS.c

    exportJson()

def updateToDay():
    global cDay, cHour, Centrales
    cDay = datetime.date.today().day

    Centrales = getCent()

    updateToHour()

    exportJson()

updateToDay()

# start
# it doesn't update if the month changes but the day doesnt, but that's not expected to happen
# will look into a better way of doing this
while True:
    if datetime.date.today().day != cDay:
        updateToDay()
    
    if datetime.datetime.today().hour != cHour:
        updateToHour()

    time.sleep(1) # check every 1 second
