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

def isOn(number):
    if number == 0:
        return 0
    else:
        return 1

def getCent():
    parsedData = dt.parseData()

    while not parsedData[0]: # If first argument is false there was an an error
        logging.error(str(parsedData[1]))
        print(str(parsedData[1]))
        time.sleep(retryWait)
        parsedData = dt.parseData()

    return(parsedData[1])

def exportMatrixBin():
    mat = array.array('B')
    lights = [0]*56
    
    for i in range(0, len(Centrales)):
        lights[i] = isOn(Centrales[i].get(cHour))
    
    mat.fromlist(lights)

    file = open(path + "matSdata.bin", 'wb')
    mat.tofile(file)
    file.close()

def exportMatrix():
    lights = [0]*64

    for i in range(0, len(Centrales)):
        lights[i] = isOn(Centrales[i].get(cHour))
    
    mat = [[lights[x+y*8] for x in range(0, 8)] for y in range(0,8)]

    file = open(path + "matSdata.txt", 'w')
    file.write(str(mat))
    file.close()

def exportJson():
    jsonData = open(path + "data.json", 'w')
    jsonCentrales = list(map(lambda x: vars(x), Centrales))
    json.dump(jsonCentrales,jsonData,indent=2)
    jsonData.close()

def updateToHour():
    global cHour
    cHour = datetime.datetime.today().hour

    #exportMatrix()
    exportMatrixBin()

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
while True:
    if datetime.date.today().day != cDay:
        updateToDay()
    
    if datetime.datetime.today().hour != cHour:
        updateToHour()

    time.sleep(1) # check every 1 second
