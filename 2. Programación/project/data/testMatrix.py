deployed = False

import RPi.GPIO as GPIO
import time
import threading
import dataTranslate

CentralesOrder = dataTranslate.CentralesOrder

GPIO.setmode(GPIO.BOARD)

global matrix
matrix = [[0]*8 for x in range(0,8)]

row = [11, 7, 5, 3, 37, 35, 33, 31]
column = [18, 22, 24, 26, 32, 36, 38, 40]

for i in row + column:
    GPIO.setup(i, GPIO.OUT)

def alloff():
    for i in row: 
        GPIO.output(i, False) 
    for x in column: 
        GPIO.output(x, not deployed) 


running = True
def updateleds():
    global matrix, running
    while running:
        alloff();
        for x in range(0,8): 
            if 1 in matrix[x]: 
                alloff() 
                GPIO.output(row[x], True) 
                for i in range(0,7): 
                    if matrix[x][i] == 1: 
                        GPIO.output(column[i], deployed) 
                time.sleep((1/60.0)/8.0) 

ledsThread = threading.Thread(target=updateleds)
ledsThread.start()

for r in range(0, 8):
    for c in range(0,7):
        if c+r*7 < len(CentralesOrder):
            print(CentralesOrder[c+r*7])

            matrix = [[0]*8 for x in range(0,8)]
            matrix[r][c] = 1

            # Fixes
            matrix[3][0] = matrix[1][1] 
            matrix[2][6] = matrix[1][3] 

            input()

running = False

GPIO.cleanup()