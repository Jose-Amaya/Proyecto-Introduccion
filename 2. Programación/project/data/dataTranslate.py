import os

deployed = os.name == 'posix'

if deployed:
    path = "/home/pi/project/data/files/" ## Informacion despacho nacional
else:
    path = os.getcwd() + "\\2. Programación\\project\\data\\files\\" ## Informacion despacho nacional

import re
import ast
import dataGet as dg
import time

class Central():
    def __init__(self, id, name, DN, OI):
        self.id = id
        self.name = name
        self.DNlist = DN
        self.OIlist = OI
        self.DNgen = [0]*24
        self.OIgen = [0]*24
        self.DNfound = False
        self.OIfound = False
        self.ActualGen = 0
    
    def get(self, hour, type = 0): # 0 = DN, other = OI
        if type is 0:
            if self.DNfound:
                self.ActualGen = self.DNgen[hour]
                return(self.DNgen[hour])
            else:
                self.ActualGen = self.OIgen[hour]
                return(self.OIgen[hour])
        else:
            if self.OIfound:
                self.ActualGen = self.OIgen[hour]
                return(self.OIgen[hour])
            else:
                self.ActualGen = self.DNgen[hour]
                return(Self.DNgen[hour])


#Lista de centrales, [ID, NAME, [DN NAME 1, ...], [OI NAME 1, ...]] # about DN NAME and OI NAME, we use regex, so escape any special character
CentralesRaw = [['E1', 'JEPIRACHI1', ['MJEPIRAC'], ['JEPIRACHI1-15']], ['T1', 'FLORES', ['FLORES IV', 'FLORES1'], ['FLORES1', 'FLORES4B']], ['T2', 'BARRANQUILLA', ['TEBSA'], ['BARRANQUILLA3', 'BARRANQUILLA4', 'TEBSAB']], ['T3', 'GUAJIRA', ['GUAJIR11', 'GUAJIR21'], ['GUAJIRA1', 'GUAJIRA2']], ['T4', 'TASAJERO', ['TASAJER1', 'TASAJERO2'], ['TASAJERO1', 'TASAJERO2']], ['T12', 'TERMOSIERRAB', ['TSIERRA'], ['TERMOSIERRAB']], ['T6', 'TERMOEMCALI1', ['TEMCALI'], ['TERMOEMCALI1']], ['T7', 'PAIPA', ['PAIPA1', 'PAIPA2', 'PAIPA3', 'PAIPA4'], ['PAIPA1', 'PAIPA2', 'PAIPA3', 'PAIPA4']], ['T8', 'TERMOCENTROCC', ['TCENTRO1'], ['TERMOCENTROCC']], ['T9', 'ZIPAEMG', ['ZIPAEMG2', 'ZIPAEMG3', 'ZIPAEMG4', 'ZIPAEMG5'], ['ZIPAEMG2', 'ZIPAEMG3', 'ZIPAEMG4', 'ZIPAEMG5']], ['T10', 'CARTAGENA', ['CTGEMG1', 'CTGEMG2', 'CTGEMG3'], ['CARTAGENA1', 'CARTAGENA2', 'CARTAGENA3']], ['T11', 'MERILECTRICA1', ['MERILEC1'], ['MERILECTRICA1']], ['H1', 'LAHERRADURA', ['LAHERRADURA'], ['LAHERRADURA1', 'LAHERRADURA2']], ['H2', 'JAGUAS', ['JAGUAS'], ['JAGUAS1', 'JAGUAS2']], ['H3', 'SANCARLOS', ['CSANCARLOS'], ['SANCARLOS1', 'SANCARLOS2', 'SANCARLOS3', 'SANCARLOS4', 'SANCARLOS5', 'SANCARLOS6', 'SANCARLOS7', 'SANCARLOS8']], ['H4', 'SOGAMOSO', ['SOGAMOSO'], ['SOGAMOSO1', 'SOGAMOSO2', 'SOGAMOSO3']], ['H5', 'AMOYALAESPERANZA', ['AMOYA'], ['AMOYALAESPERANZA1', 'AMOYALAESPERANZA2']], ['H6', 'MIELI', ['MIEL1'], ['MIELI1', 'MIELI2', 'MIELI3']], ['H7', 'CALDERAS', ['MCALDERAS'], ['CALDERAS1', 'CALDERAS2']], ['H8', 'GUAVIO', ['GUAVIO', 'MGUAVIO'], ['GUAVIO1', 'GUAVIO2', 'GUAVIO3', 'GUAVIO4', 'GUAVIO5']], ['H9', 'BETANIA', ['BETANIA'], ['BETANIA1', 'BETANIA2', 'BETANIA3']], ['H10', 'ELQUIMBO', ['ELQUIMBO'], ['ELQUIMBO1', 'ELQUIMBO2']], ['H11', 'PARAISO', ['PAGUA'], ['PARAISO1', 'PARAISO2', 'PARAISO3']], ['H12', 'LAGUACA', ['PAGUA'], ['LAGUACA1', 'LAGUACA2', 'LAGUACA3']], ['H13', 'TEQUENDAMA', ['MB_TEQUENDA','MTEQUEND1','MTEQUEND2','MTEQUEND3','MTEQUEND4'], ['TEQUENDAMA1','TEQUENDAMA2','TEQUENDAMA3','TEQUENDAMA4']], ['H14', 'LATASAJERA', ['LATASAJERA'], ['LATASAJERA1', 'LATASAJERA2', 'LATASAJERA3']], ['H15', 'CARACOLI', ['MCARACOLI'], ['CARACOLI']], ['H16', 'ELLIMONAR', ['MLIMONAR'], ['ELLIMONAR']], ['H17', 'DARIOVALENCIASAMPER', ['DARIOVS'], ['DARIOVALENCIASAMPER1', 'DARIOVALENCIASAMPER2', 'DARIOVALENCIASAMPER5']], ['H18', 'LAGUNETA', ['MLAGUNETA'], ['LAGUNETA']], ['H19', 'PAJARITO', ['MPAJARITO'], ['PAJARITO1','PAJARITO2']], ['H20', 'SANJOSEDELAMONTANA', ['MSNJOSE_MONT'], ['SANJOSEDELAMONTAÑA','SANJOSEDELAMONTAÑAII1']], ['H1', 'TRONERAS', ['GUATRON'], ['TRONERAS1', 'TRONERAS2']], ['H2', 'GUADALUPE3', [], ['GUADALUPE31', 'GUADALUPE32', 'GUADALUPE33', 'GUADALUPE34', 'GUADALUPE35', 'GUADALUPE36']], ['H3', 'GUADALUPE4', [], ['GUADALUPE41', 'GUADALUPE42', 'GUADALUPE43']], ['H4', 'PORCEII', ['PORCE2'], ['PORCEII1', 'PORCEII2', 'PORCEII3']], ['H5', 'PORCEIII', ['PORCE3'], ['PORCEIII4', 'PORCEIII3', 'PORCEIII2', 'PORCEIII1']], ['H6', 'GUATAPE', ['GUATAPE'], ['GUATAPE1', 'GUATAPE2', 'GUATAPE3', 'GUATAPE4', 'GUATAPE5', 'GUATAPE6', 'GUATAPE7', 'GUATAPE8']], ['H7', 'RIOABAJO', [], []], ['H8', 'SONSON', ['MSONSON'], ['SONSON']], ['H9', 'RIOFRIO(TAMESIS)', ['MRFRIOTAMES','MRIOFRIO1','RIOFRIO2'], ['RIOFRIO\(TAMESIS\)']], ['H10', 'AYURA', ['M_AYURA'], ['AYURA']], ['H11', 'NIQUIA', ['MNIQUIA'], ['NIQUIA']], ['H12', 'URRA1', ['URRA'], ['URRA1']], ['H13', 'CHIVOR', ['CHIVOR'], ['CHIVOR1', 'CHIVOR2', 'CHIVOR3', 'CHIVOR4', 'CHIVOR5', 'CHIVOR6', 'CHIVOR7', 'CHIVOR8']], ['H14', 'CUCUANA', ['CUCUANA'], ['CUCUANA1', 'CUCUANA2']], ['H15', 'CALIMA', ['CALIMA1'], ['CALIMA1', 'CALIMA2', 'CALIMA3', 'CALIMA4']]]
CentralesOrder = ['E1','T1','T2','T3','T4','T12','T6','T7','T8','T9','T10','T11','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','H14','H15','H16','H17','H18','H19','H20','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','H14','H15'];

Centrales = []

# Initialize
def initialize():
    for c in CentralesRaw:
        temp = Central(c[0], c[1], c[2], c[3])
        Centrales.append(temp)

# Add multiple lists
def listAdd(lists): # Argument is a list of lists
    z = zip(*lists)
    z = map(lambda x: sum(x), z)
    return(list(z))

def parseData():
    DNOI = dg.getData()

    dataDN = DNOI[0]
    dataOI = DNOI[1]

    if dataDN.find("ERROR DATAGET") != -1 or dataOI.find("ERROR DATAGET") != -1:
        return [False,[dataDN,dataOI]] # Means there was an error

    for i in range(0, len(Centrales)):

        # Despacho nacional

        if len(Centrales[i].DNlist) is not 0:

            toRegex = lambda s: '\"(?:%s)\",(.*)' % s # Regular expression to search for all the data 
            pattern = Centrales[i].DNlist[0] 
        
            for j in range(1, len(Centrales[i].DNlist)): # Put all the possible options
                pattern += "|" + Centrales[i].DNlist[j]

            pattern = toRegex(pattern)

            data = re.findall(pattern, dataDN) # Find every match

            if len(data) is 0:
                Centrales[i].DNgen = [0]*24 # If nothing is found
                Centrales[i].DNfound = False
            else:
                Centrales[i].DNgen = listAdd(list(map(lambda x: ast.literal_eval(x), data))) # The data is csv, we can eval it
                Centrales[i].DNfound = True
    
        # Oferta inicial
        
        if len(Centrales[i].OIlist) is not 0:
            toRegex = lambda s: '(?:%s) , D, *(.*)' % s 
            pattern = Centrales[i].OIlist[0]
        
            for j in range(1, len(Centrales[i].OIlist)):
                pattern += "|" + Centrales[i].OIlist[j]

            pattern = toRegex(pattern)

            data = re.findall(pattern, dataOI)
        
            if len(data) is 0:
                Centrales[i].OIgen = [0]*24
                Centrales[i].OIfound = False
            else:
                Centrales[i].OIgen = listAdd(list(map(lambda x: ast.literal_eval(x), data)))
                Centrales[i].OIfound = True

    return([True,Centrales])

initialize()