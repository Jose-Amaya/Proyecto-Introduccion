deployed = False

import RPi.GPIO as GPIO
import time
import threading

CentralesOrder = ['E1','T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','H14','H15','H16','H17','H18','H19','H20','H21','H22','H23','H24','H25','H26','H27','H28','H29','H30','H31','H32','H33','H34','H35'];

GPIO.setmode(GPIO.BOARD)

for i in row + column:
    GPIO.setup(i, GPIO.OUT)

global matrix

row = [11, 7, 5, 3, 37, 35, 33, 31]
column = [18, 22, 24, 26, 32, 36, 38, 40]

def alloff():
    for i in row: 
        GPIO.output(i, False) 
    for x in column: 
        GPIO.output(x, not deployed) 

def updateleds(): 
    global matrix
    alloff();
    for x in range(0,8): 
        if 1 in matrix[x]: 
            alloff() 
            GPIO.output(row[x], True) 
            for i in range(0,7): 
                if matrix[x][i] == 1: 
                    GPIO.output(column[i], deployed) 
            time.sleep((1/60.0)/8.0) 

threading.Thread(target=updateleds).start()

for r in range(0, 8):
    for c in range(0,7):
        alloff()

        matrix = [[0]*8 for x in range(0,8)]
        matrix[r][c] = 1

        # Fixes
        matrix[3][0] = matrix[1][1] 
        matrix[2][6] = matrix[1][3] 

        time.sleep(0.2)

GPIO.cleanup()