
# coding: utf-8
# Este programa actualiza un archivo de texto, con tantas filas como centrales, y cada fila con 24 numeros, siendo 1s o 0s, definiendo el estado de la central para las 24 horas
# In[1]:


import datetime
import time
import numpy as np

matrix=np.zeros((47,24))
v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

file=open("data.txt")
file2=open("Leds.txt","w")
plantasG=file.readlines()
for i in range(0,217):
    if plantasG[i].find("MJEPIRAC",0,len(plantasG[i]))!=-1:
        fila=plantasG[i]
        m=0
        for j in range(0,24):
            p=fila.find(",",m,len(fila))                            #0
            if ord(fila[p+1])!=48:
                matrix[0,j]=1
            else:
                matrix[0,j]=0
            m=p+1
    else:
        if plantasG[i].find("FLORES IV",0,len(plantasG[i]))!=-1:
            fila=plantasG[i]
            m=0
            for j in range(0,24):
                p=fila.find(",",m,len(fila))
                if ord(fila[p+1])!=48:                             #1
                    v1.append(1)
                else:
                    v1.append(0)
                m=p+1
        else:
            if plantasG[i].find("FLORES1",0,len(plantasG[i]))!=-1:
                fila=plantasG[i]
                m=0
                for j in range(0,24):
                    p=fila.find(",",m,len(fila))
                    if ord(fila[p+1])!=48:                      #1    
                        v2.append(1)
                    else:
                        v2.append(0)
                    m=p+1
            else:
                if plantasG[i].find("TEBSA",0,len(plantasG[i]))!=-1:
                    fila=plantasG[i]
                    m=0
                    for j in range(0,24):
                        p=fila.find(",",m,len(fila))
                        if ord(fila[p+1])!=48:                   #2
                            matrix[2,j]=1
                        else:
                            matrix[2,j]=0
                        m=p+1
                else:
                    if plantasG[i].find("GUAJIR11",0,len(plantasG[i]))!=-1:
                        fila=plantasG[i]
                        m=0
                        for j in range(0,24):
                            p=fila.find(",",m,len(fila))
                            if ord(fila[p+1])!=48:                    #3
                                v3.append(1)
                            else:
                                v3.append(0)
                            m=p+1
                    else:
                        if plantasG[i].find("GUAJIR21",0,len(plantasG[i]))!=-1:
                            fila=plantasG[i]
                            m=0
                            for j in range(0,24):
                                p=fila.find(",",m,len(fila))
                                if ord(fila[p+1])!=48:
                                    v4.append(1)                           #3
                                else:
                                    v4.append(0)
                                m=p+1
                        else:
                            if plantasG[i].find("TASAJER1",0,len(plantasG[i]))!=-1:
                                fila=plantasG[i]
                                m=0
                                for j in range(0,24):
                                    p=fila.find(",",m,len(fila))
                                    if ord(fila[p+1])!=48:                  #4
                                        v5.append(1)
                                    else:
                                        v5.append(0)
                                    m=p+1
                            else:
                                if plantasG[i].find("TASAJERO2",0,len(plantasG[i]))!=-1:
                                    fila=plantasG[i]
                                    m=0
                                    for j in range(0,24):
                                        p=fila.find(",",m,len(fila))
                                        if ord(fila[p+1])!=48:                  #4
                                            v6.append(1)
                                        else:
                                            v6.append(0)
                                        m=p+1
                                else:
                                    if plantasG[i].find("TSIERRA",0,len(plantasG[i]))!=-1:
                                        fila=plantasG[i]
                                        m=0
                                        for j in range(0,24):
                                            p=fila.find(",",m,len(fila))
                                            if ord(fila[p+1])!=48:                  #5
                                                matrix[5,j]=1
                                            else:
                                                matrix[5,j]=0
                                            m=p+1
                                    else:
                                        if plantasG[i].find("TEMCALI",0,len(plantasG[i]))!=-1:
                                            fila=plantasG[i]
                                            m=0
                                            for j in range(0,24):
                                                p=fila.find(",",m,len(fila))
                                                if ord(fila[p+1])!=48:                  #6
                                                    matrix[6,j]=1
                                                else:
                                                    matrix[6,j]=0
                                                m=p+1
                                        else:
                                            if plantasG[i].find("PAIPA1",0,len(plantasG[i]))!=-1:
                                                fila=plantasG[i]
                                                m=0
                                                for j in range(0,24):
                                                    p=fila.find(",",m,len(fila))
                                                    if ord(fila[p+1])!=48:                  #7
                                                        v7.append(1)
                                                    else:
                                                        v7.append(0)
                                                    m=p+1
                                            else:
                                                if plantasG[i].find("PAIPA2",0,len(plantasG[i]))!=-1:
                                                    fila=plantasG[i]
                                                    m=0
                                                    for j in range(0,24):
                                                        p=fila.find(",",m,len(fila))
                                                        if ord(fila[p+1])!=48:                  #7
                                                            v8.append(1)
                                                        else:
                                                            v8.append(0)
                                                        m=p+1
                                                else:
                                                    if plantasG[i].find("PAIPA3",0,len(plantasG[i]))!=-1:
                                                        fila=plantasG[i]
                                                        m=0
                                                        for j in range(0,24):
                                                            p=fila.find(",",m,len(fila))
                                                            if ord(fila[p+1])!=48:                  #7
                                                                v9.append(1)
                                                            else:
                                                                v9.append(0)
                                                            m=p+1
                                                    else:
                                                        if plantasG[i].find("PAIPA4",0,len(plantasG[i]))!=-1:
                                                            fila=plantasG[i]
                                                            m=0
                                                            for j in range(0,24):
                                                                p=fila.find(",",m,len(fila))
                                                                if ord(fila[p+1])!=48:                  #7
                                                                    v10.append(1)
                                                                else:
                                                                    v10.append(0)
                                                                m=p+1
                                                        else:
                                                            if plantasG[i].find("TCENTRO1",0,len(plantasG[i]))!=-1:
                                                                fila=plantasG[i]
                                                                m=0
                                                                for j in range(0,24):
                                                                    p=fila.find(",",m,len(fila))
                                                                    if ord(fila[p+1])!=48:                  #8
                                                                        matrix[8,j]=1
                                                                    else:
                                                                        matrix[8,j]=0
                                                                    m=p+1
                                                            else:
                                                                if plantasG[i].find("ZIPAEMG2",0,len(plantasG[i]))!=-1:
                                                                    fila=plantasG[i]
                                                                    m=0
                                                                    for j in range(0,24):
                                                                        p=fila.find(",",m,len(fila))
                                                                        if ord(fila[p+1])!=48:                  #9
                                                                            v11.append(1)
                                                                        else:
                                                                            v11.append(0)
                                                                        m=p+1
                                                                else:
                                                                    if plantasG[i].find("ZIPAEMG3",0,len(plantasG[i]))!=-1:
                                                                        fila=plantasG[i]
                                                                        m=0
                                                                        for j in range(0,24):
                                                                            p=fila.find(",",m,len(fila))
                                                                            if ord(fila[p+1])!=48:                  #9
                                                                                v12.append(1)
                                                                            else:
                                                                                v12.append(0)
                                                                            m=p+1
                                                                    else:
                                                                        if plantasG[i].find("ZIPAEMG4",0,len(plantasG[i]))!=-1:
                                                                            fila=plantasG[i]
                                                                            m=0
                                                                            for j in range(0,24):
                                                                                p=fila.find(",",m,len(fila))
                                                                                if ord(fila[p+1])!=48:                  #9
                                                                                    v13.append(1)
                                                                                else:
                                                                                    v13.append(0)
                                                                                m=p+1
                                                                        else:
                                                                            if plantasG[i].find("ZIPAEMG5",0,len(plantasG[i]))!=-1:
                                                                                fila=plantasG[i]
                                                                                m=0
                                                                                for j in range(0,24):
                                                                                    p=fila.find(",",m,len(fila))
                                                                                    if ord(fila[p+1])!=48:                  #9
                                                                                        v14.append(1)
                                                                                    else:
                                                                                        v14.append(0)
                                                                                    m=p+1
                                                                            else:
                                                                                if plantasG[i].find("CTGEMG1",0,len(plantasG[i]))!=-1:
                                                                                    fila=plantasG[i]
                                                                                    m=0
                                                                                    for j in range(0,24):
                                                                                        p=fila.find(",",m,len(fila))
                                                                                        if ord(fila[p+1])!=48:                  #10
                                                                                            v15.append(1)
                                                                                        else:
                                                                                            v15.append(0)
                                                                                        m=p+1
                                                                                else:
                                                                                    if plantasG[i].find("CTGEMG2",0,len(plantasG[i]))!=-1:
                                                                                        fila=plantasG[i]
                                                                                        m=0
                                                                                        for j in range(0,24):
                                                                                            p=fila.find(",",m,len(fila))
                                                                                            if ord(fila[p+1])!=48:                  #10
                                                                                                v16.append(1)
                                                                                            else:
                                                                                                v16.append(0)
                                                                                            m=p+1
                                                                                    else:
                                                                                        if plantasG[i].find("CTGEMG3",0,len(plantasG[i]))!=-1:
                                                                                            fila=plantasG[i]
                                                                                            m=0
                                                                                            for j in range(0,24):
                                                                                                p=fila.find(",",m,len(fila))
                                                                                                if ord(fila[p+1])!=48:                  #10
                                                                                                    v17.append(1)
                                                                                                else:
                                                                                                    v17.append(0)
                                                                                                m=p+1
                                                                                        else:
                                                                                            if plantasG[i].find("MERILEC1",0,len(plantasG[i]))!=-1:
                                                                                                fila=plantasG[i]
                                                                                                m=0
                                                                                                for j in range(0,24):
                                                                                                    p=fila.find(",",m,len(fila))
                                                                                                    if ord(fila[p+1])!=48:                  #11
                                                                                                        matrix[11,j]=1
                                                                                                    else:
                                                                                                        matrix[11,j]=0
                                                                                                    m=p+1
                                                                                            else:
                                                                                                if plantasG[i].find("LAHERRADURA",0,len(plantasG[i]))!=-1:
                                                                                                    fila=plantasG[i]
                                                                                                    m=0
                                                                                                    for j in range(0,24):
                                                                                                        p=fila.find(",",m,len(fila))
                                                                                                        if ord(fila[p+1])!=48:                  #12
                                                                                                            matrix[12,j]=1
                                                                                                        else:
                                                                                                            matrix[12,j]=0
                                                                                                        m=p+1
                                                                                                else:
                                                                                                    if plantasG[i].find("JAGUAS",0,len(plantasG[i]))!=-1:
                                                                                                        fila=plantasG[i]
                                                                                                        m=0
                                                                                                        for j in range(0,24):
                                                                                                            p=fila.find(",",m,len(fila))
                                                                                                            if ord(fila[p+1])!=48:                  #13
                                                                                                                matrix[13,j]=1
                                                                                                            else:
                                                                                                                matrix[13,j]=0
                                                                                                            m=p+1
                                                                                                    else:
                                                                                                        if plantasG[i].find("CSANCARLOS",0,len(plantasG[i]))!=-1:
                                                                                                            fila=plantasG[i]
                                                                                                            m=0
                                                                                                            for j in range(0,24):
                                                                                                                p=fila.find(",",m,len(fila))
                                                                                                                if ord(fila[p+1])!=48:                  #14
                                                                                                                    matrix[14,j]=1
                                                                                                                else:
                                                                                                                    matrix[14,j]=0
                                                                                                                m=p+1
                                                                                                        else:
                                                                                                            if plantasG[i].find("SOGAMOSO",0,len(plantasG[i]))!=-1:
                                                                                                                fila=plantasG[i]
                                                                                                                m=0
                                                                                                                for j in range(0,24):
                                                                                                                    p=fila.find(",",m,len(fila))
                                                                                                                    if ord(fila[p+1])!=48:                  #15
                                                                                                                        matrix[15,j]=1
                                                                                                                    else:
                                                                                                                        matrix[15,j]=0
                                                                                                                    m=p+1
                                                                                                            else:
                                                                                                                if plantasG[i].find("AMOYA",0,len(plantasG[i]))!=-1:
                                                                                                                    fila=plantasG[i]
                                                                                                                    m=0
                                                                                                                    for j in range(0,24):
                                                                                                                        p=fila.find(",",m,len(fila))
                                                                                                                        if ord(fila[p+1])!=48:                  #16
                                                                                                                            matrix[16,j]=1
                                                                                                                        else:
                                                                                                                            matrix[16,j]=0
                                                                                                                        m=p+1
                                                                                                                else:
                                                                                                                    if plantasG[i].find("MIEL1",0,len(plantasG[i]))!=-1:
                                                                                                                        fila=plantasG[i]
                                                                                                                        m=0
                                                                                                                        for j in range(0,24):
                                                                                                                            p=fila.find(",",m,len(fila))
                                                                                                                            if ord(fila[p+1])!=48:                  #17
                                                                                                                                matrix[17,j]=1
                                                                                                                            else:
                                                                                                                                matrix[17,j]=0
                                                                                                                            m=p+1
                                                                                                                    else:
                                                                                                                        if plantasG[i].find("MCALDERAS",0,len(plantasG[i]))!=-1:
                                                                                                                            fila=plantasG[i]
                                                                                                                            m=0
                                                                                                                            for j in range(0,24):
                                                                                                                                p=fila.find(",",m,len(fila))
                                                                                                                                if ord(fila[p+1])!=48:                  #18
                                                                                                                                    matrix[18,j]=1
                                                                                                                                else:
                                                                                                                                    matrix[18,j]=0
                                                                                                                                m=p+1
                                                                                                                        else:
                                                                                                                            if plantasG[i].find("GUAVIO",0,len(plantasG[i]))!=-1:
                                                                                                                                fila=plantasG[i]
                                                                                                                                m=0
                                                                                                                                for j in range(0,24):
                                                                                                                                    p=fila.find(",",m,len(fila))
                                                                                                                                    if ord(fila[p+1])!=48:                  #19
                                                                                                                                        matrix[19,j]=1
                                                                                                                                    else:
                                                                                                                                        matrix[19,j]=0
                                                                                                                                    m=p+1
                                                                                                                            else:
                                                                                                                                if plantasG[i].find("BETANIA",0,len(plantasG[i]))!=-1:
                                                                                                                                    fila=plantasG[i]
                                                                                                                                    m=0
                                                                                                                                    for j in range(0,24):
                                                                                                                                        p=fila.find(",",m,len(fila))
                                                                                                                                        if ord(fila[p+1])!=48:                  #20
                                                                                                                                            matrix[20,j]=1
                                                                                                                                        else:
                                                                                                                                            matrix[20,j]=0
                                                                                                                                        m=p+1
                                                                                                                                else:
                                                                                                                                    if plantasG[i].find("ELQUIMBO",0,len(plantasG[i]))!=-1:
                                                                                                                                        fila=plantasG[i]
                                                                                                                                        m=0
                                                                                                                                        for j in range(0,24):
                                                                                                                                            p=fila.find(",",m,len(fila))
                                                                                                                                            if ord(fila[p+1])!=48:                  #21
                                                                                                                                                matrix[21,j]=1
                                                                                                                                            else:
                                                                                                                                                matrix[21,j]=0
                                                                                                                                            m=p+1
                                                                                                                                    else:
                                                                                                                                        if plantasG[i].find("PAGUA",0,len(plantasG[i]))!=-1:
                                                                                                                                            fila=plantasG[i]
                                                                                                                                            m=0
                                                                                                                                            for j in range(0,24):
                                                                                                                                                p=fila.find(",",m,len(fila))
                                                                                                                                                if ord(fila[p+1])!=48:                  #22 y 23
                                                                                                                                                     matrix[22,j]=1
                                                                                                                                                     matrix[23,j]=1
                                                                                                                                                else:
                                                                                                                                                     matrix[22,j]=0
                                                                                                                                                     matrix[23,j]=0
                                                                                                                                                m=p+1
                                                                                                                                        else:
                                                                                                                                            if plantasG[i].find("MTEQUENDAMA",0,len(plantasG[i]))!=-1:
                                                                                                                                                fila=plantasG[i]
                                                                                                                                                m=0
                                                                                                                                                for j in range(0,24):
                                                                                                                                                    p=fila.find(",",m,len(fila))
                                                                                                                                                    if ord(fila[p+1])!=48:                  #24
                                                                                                                                                         matrix[24,j]=1
                                                                                                                                                    else:
                                                                                                                                                         matrix[24,j]=0
                                                                                                                                                    m=p+1
                                                                                                                                            else:
                                                                                                                                                if plantasG[i].find("LATASAJERA",0,len(plantasG[i]))!=-1:
                                                                                                                                                    fila=plantasG[i]
                                                                                                                                                    m=0
                                                                                                                                                    for j in range(0,24):
                                                                                                                                                        p=fila.find(",",m,len(fila))
                                                                                                                                                        if ord(fila[p+1])!=48:                  #25
                                                                                                                                                             matrix[25,j]=1
                                                                                                                                                        else:
                                                                                                                                                             matrix[25,j]=0
                                                                                                                                                        m=p+1
                                                                                                                                                else:
                                                                                                                                                    if plantasG[i].find("MCARACOLI",0,len(plantasG[i]))!=-1:
                                                                                                                                                        fila=plantasG[i]
                                                                                                                                                        m=0
                                                                                                                                                        for j in range(0,24):
                                                                                                                                                            p=fila.find(",",m,len(fila))
                                                                                                                                                            if ord(fila[p+1])!=48:                  #26
                                                                                                                                                                 matrix[26,j]=1
                                                                                                                                                            else:
                                                                                                                                                                 matrix[26,j]=0
                                                                                                                                                            m=p+1
                                                                                                                                                    else:
                                                                                                                                                        if plantasG[i].find("MLIMONAR",0,len(plantasG[i]))!=-1:
                                                                                                                                                            fila=plantasG[i]
                                                                                                                                                            m=0
                                                                                                                                                            for j in range(0,24):
                                                                                                                                                                p=fila.find(",",m,len(fila))
                                                                                                                                                                if ord(fila[p+1])!=48:                  #27
                                                                                                                                                                     matrix[27,j]=1
                                                                                                                                                                else:
                                                                                                                                                                     matrix[27,j]=0
                                                                                                                                                                m=p+1
                                                                                                                                                        else:
                                                                                                                                                            if plantasG[i].find("DARIOVS",0,len(plantasG[i]))!=-1:
                                                                                                                                                                fila=plantasG[i]
                                                                                                                                                                m=0
                                                                                                                                                                for j in range(0,24):
                                                                                                                                                                    p=fila.find(",",m,len(fila))
                                                                                                                                                                    if ord(fila[p+1])!=48:                  #28
                                                                                                                                                                         matrix[28,j]=1
                                                                                                                                                                    else:
                                                                                                                                                                         matrix[28,j]=0
                                                                                                                                                                    m=p+1
                                                                                                                                                            else:
                                                                                                                                                                if plantasG[i].find("MLAGUNETA",0,len(plantasG[i]))!=-1:
                                                                                                                                                                    fila=plantasG[i]
                                                                                                                                                                    m=0
                                                                                                                                                                    for j in range(0,24):
                                                                                                                                                                        p=fila.find(",",m,len(fila))
                                                                                                                                                                        if ord(fila[p+1])!=48:                  #29
                                                                                                                                                                             matrix[29,j]=1
                                                                                                                                                                        else:
                                                                                                                                                                             matrix[29,j]=0
                                                                                                                                                                        m=p+1
                                                                                                                                                                else:
                                                                                                                                                                    if plantasG[i].find("MPAJARITO",0,len(plantasG[i]))!=-1:
                                                                                                                                                                        fila=plantasG[i]
                                                                                                                                                                        m=0
                                                                                                                                                                        for j in range(0,24):
                                                                                                                                                                            p=fila.find(",",m,len(fila))
                                                                                                                                                                            if ord(fila[p+1])!=48:                  #30
                                                                                                                                                                                 matrix[30,j]=1
                                                                                                                                                                            else:
                                                                                                                                                                                 matrix[30,j]=0
                                                                                                                                                                            m=p+1
                                                                                                                                                                    else:
                                                                                                                                                                        if plantasG[i].find("MSNJOSE_MONT",0,len(plantasG[i]))!=-1:
                                                                                                                                                                            fila=plantasG[i]
                                                                                                                                                                            m=0
                                                                                                                                                                            for j in range(0,24):
                                                                                                                                                                                p=fila.find(",",m,len(fila))
                                                                                                                                                                                if ord(fila[p+1])!=48:                  #31
                                                                                                                                                                                     matrix[31,j]=1
                                                                                                                                                                                else:
                                                                                                                                                                                     matrix[31,j]=0
                                                                                                                                                                                m=p+1
                                                                                                                                                                        else:
                                                                                                                                                                            if plantasG[i].find("GUATRON",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                fila=plantasG[i]
                                                                                                                                                                                m=0
                                                                                                                                                                                for j in range(0,24):
                                                                                                                                                                                    p=fila.find(",",m,len(fila))
                                                                                                                                                                                    if ord(fila[p+1])!=48:                  #32
                                                                                                                                                                                         matrix[32,j]=1
                                                                                                                                                                                    else:
                                                                                                                                                                                         matrix[32,j]=0
                                                                                                                                                                                    m=p+1
                                                                                                                                                                            else:
                                                                                                                                                                                if plantasG[i].find("PORCE2",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                    fila=plantasG[i]
                                                                                                                                                                                    m=0
                                                                                                                                                                                    for j in range(0,24):
                                                                                                                                                                                        p=fila.find(",",m,len(fila))
                                                                                                                                                                                        if ord(fila[p+1])!=48:                  #35
                                                                                                                                                                                             matrix[35,j]=1
                                                                                                                                                                                        else:
                                                                                                                                                                                             matrix[35,j]=0
                                                                                                                                                                                        m=p+1
                                                                                                                                                                                else:
                                                                                                                                                                                    if plantasG[i].find("PORCE3",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                        fila=plantasG[i]
                                                                                                                                                                                        m=0
                                                                                                                                                                                        for j in range(0,24):
                                                                                                                                                                                            p=fila.find(",",m,len(fila))
                                                                                                                                                                                            if ord(fila[p+1])!=48:                  #36
                                                                                                                                                                                                 matrix[36,j]=1
                                                                                                                                                                                            else:
                                                                                                                                                                                                 matrix[36,j]=0
                                                                                                                                                                                            m=p+1
                                                                                                                                                                                    else:
                                                                                                                                                                                        if plantasG[i].find("GUATAPE",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                            fila=plantasG[i]
                                                                                                                                                                                            m=0
                                                                                                                                                                                            for j in range(0,24):
                                                                                                                                                                                                p=fila.find(",",m,len(fila))
                                                                                                                                                                                                if ord(fila[p+1])!=48:                  #37
                                                                                                                                                                                                     matrix[37,j]=1
                                                                                                                                                                                                else:
                                                                                                                                                                                                     matrix[37,j]=0
                                                                                                                                                                                                m=p+1
                                                                                                                                                                                        else:
                                                                                                                                                                                            if plantasG[i].find("MRIOABAJO",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                                fila=plantasG[i]
                                                                                                                                                                                                m=0
                                                                                                                                                                                                for j in range(0,24):
                                                                                                                                                                                                    p=fila.find(",",m,len(fila))
                                                                                                                                                                                                    if ord(fila[p+1])!=48:                  #38
                                                                                                                                                                                                         matrix[38,j]=1
                                                                                                                                                                                                    else:
                                                                                                                                                                                                         matrix[38,j]=0
                                                                                                                                                                                                    m=p+1
                                                                                                                                                                                            else:
                                                                                                                                                                                                if plantasG[i].find("MSONSON",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                                    fila=plantasG[i]
                                                                                                                                                                                                    m=0
                                                                                                                                                                                                    for j in range(0,24):
                                                                                                                                                                                                        p=fila.find(",",m,len(fila))
                                                                                                                                                                                                        if ord(fila[p+1])!=48:                  #39
                                                                                                                                                                                                             matrix[39,j]=1
                                                                                                                                                                                                        else:
                                                                                                                                                                                                             matrix[39,j]=0
                                                                                                                                                                                                        m=p+1
                                                                                                                                                                                                else:
                                                                                                                                                                                                    if plantasG[i].find("MRFRIOTAMES",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                                        fila=plantasG[i]
                                                                                                                                                                                                        m=0
                                                                                                                                                                                                        for j in range(0,24):
                                                                                                                                                                                                            p=fila.find(",",m,len(fila))
                                                                                                                                                                                                            if ord(fila[p+1])!=48:                  #40
                                                                                                                                                                                                                 matrix[40,j]=1
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                 matrix[40,j]=0
                                                                                                                                                                                                            m=p+1
                                                                                                                                                                                                    else:
                                                                                                                                                                                                        if plantasG[i].find("M_AYURA",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                                            fila=plantasG[i]
                                                                                                                                                                                                            m=0
                                                                                                                                                                                                            for j in range(0,24):
                                                                                                                                                                                                                p=fila.find(",",m,len(fila))
                                                                                                                                                                                                                if ord(fila[p+1])!=48:                  #41
                                                                                                                                                                                                                     matrix[41,j]=1
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                     matrix[41,j]=0
                                                                                                                                                                                                                m=p+1
                                                                                                                                                                                                        else:
                                                                                                                                                                                                            if plantasG[i].find("MNIQUIA",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                                                fila=plantasG[i]
                                                                                                                                                                                                                m=0
                                                                                                                                                                                                                for j in range(0,24):
                                                                                                                                                                                                                    p=fila.find(",",m,len(fila))
                                                                                                                                                                                                                    if ord(fila[p+1])!=48:                  #42
                                                                                                                                                                                                                         matrix[42,j]=1
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                         matrix[42,j]=0
                                                                                                                                                                                                                    m=p+1
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                if plantasG[i].find("URRA",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                                                    fila=plantasG[i]
                                                                                                                                                                                                                    m=0
                                                                                                                                                                                                                    for j in range(0,24):
                                                                                                                                                                                                                        p=fila.find(",",m,len(fila))
                                                                                                                                                                                                                        if ord(fila[p+1])!=48:                  #43
                                                                                                                                                                                                                             matrix[43,j]=1
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                             matrix[43,j]=0
                                                                                                                                                                                                                        m=p+1
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    if plantasG[i].find("CHIVOR",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                                                        fila=plantasG[i]
                                                                                                                                                                                                                        m=0
                                                                                                                                                                                                                        for j in range(0,24):
                                                                                                                                                                                                                            p=fila.find(",",m,len(fila))
                                                                                                                                                                                                                            if ord(fila[p+1])!=48:                  #44
                                                                                                                                                                                                                                 matrix[44,j]=1
                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                 matrix[44,j]=0
                                                                                                                                                                                                                            m=p+1
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                        if plantasG[i].find("CUCUANA",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                                                            fila=plantasG[i]
                                                                                                                                                                                                                            m=0
                                                                                                                                                                                                                            for j in range(0,24):
                                                                                                                                                                                                                                p=fila.find(",",m,len(fila))
                                                                                                                                                                                                                                if ord(fila[p+1])!=48:                  #45
                                                                                                                                                                                                                                     matrix[45,j]=1
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                     matrix[45,j]=0
                                                                                                                                                                                                                                m=p+1
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            if plantasG[i].find("CALIMA1",0,len(plantasG[i]))!=-1:
                                                                                                                                                                                                                                fila=plantasG[i]
                                                                                                                                                                                                                                m=0
                                                                                                                                                                                                                                for j in range(0,24):
                                                                                                                                                                                                                                    p=fila.find(",",m,len(fila))
                                                                                                                                                                                                                                    if ord(fila[p+1])!=48:                  #46
                                                                                                                                                                                                                                         matrix[46,j]=1
                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                         matrix[46,j]=0
                                                                                                                                                                                                                                    m=p+1
                                                                                                                                                                                                                            
x1=[]
x1F=[]
for k in range(0,len(v1)):
    x1.append(v1[k]+v2[k])
    if x1[k]==0:
        x1F.append(0)
    else:
        x1F.append(1)
for l in range(0,len(x1F)):
    matrix[1,l]=x1F[l]
    
x2=[]
x2F=[]
for c in range(0,len(v1)):
    x2.append(v3[c]+v4[c])
    if x2[c]==0:
        x2F.append(0)
    else:
        x2F.append(1)
for d in range(0,len(x2F)):
    matrix[3,d]=x1F[d]
    
x3=[]
x3F=[]
for e in range(0,len(v1)):
    x3.append(v5[e]+v6[e])
    if x3[e]==0:
        x3F.append(0)
    else:
        x3F.append(1)
for f in range(0,len(x3F)):
    matrix[4,f]=x3F[f]
    
x4=[]
x4F=[]
for g in range(0,len(v1)):
    x4.append(v7[g]+v8[g]+v9[g]+v10[g])
    if x4[g]==0:
        x4F.append(0)
    else:
        x4F.append(1)
for h in range(0,len(x4F)):
    matrix[7,h]=x4F[h]
    
x5=[]
x5F=[]
for o in range(0,len(v1)):
    x5.append(v11[o]+v12[o]+v13[o]+v14[o])
    if x5[o]==0:
        x5F.append(0)
    else:
        x5F.append(1)
for q in range(0,len(x5F)):
    matrix[9,q]=x5F[q]
    
x6=[]
x6F=[]
for r in range(0,len(v1)):
    x6.append(v15[r]+v16[r]+v17[r])
    if x6[r]==0:
        x6F.append(0)
    else:
        x6F.append(1)
for s in range(0,len(x6F)):
    matrix[10,s]=x6F[s]
np.savetxt('Leds.txt',np.transpose(matrix), fmt='%1i',  delimiter=',', newline='\n')