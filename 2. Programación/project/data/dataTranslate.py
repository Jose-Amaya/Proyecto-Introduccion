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
    def __init__(self, id, name, mapName, DN, OI, index):
        self.id = id
        self.name = name
        self.mapName = mapName

        self.DNlist = DN
        self.OIlist = OI

        self.DNgen = [0]*24
        self.OIgen = [0]*24

        self.DNfound = False
        self.OIfound = False

        self.currentGen = 0

        self.index = index
        
    
    def get(self, hour, type = 0): # 0 = DN, other = OI
        if type is 0:
            if self.DNfound:
                self.currentGen = self.DNgen[hour]
                return(self.DNgen[hour])
            else:
                self.currentGen = self.OIgen[hour]
                return(self.OIgen[hour])
        else:
            if self.OIfound:
                self.currentGen = self.OIgen[hour]
                return(self.OIgen[hour])
            else:
                self.currentGen = self.DNgen[hour]
                return(Self.DNgen[hour])


#Lista de centrales, [ID, NAME, [DN NAME 1, ...], [OI NAME 1, ...]] # about DN NAME and OI NAME, we use regex, so escape any special character
CentralesRaw = [['E1', 'JEPIRACHI1', 'Parque Eolico De Jepirachi', ['MJEPIRAC'], ['JEPIRACHI1-15']], ['T1', 'FLORES', 'Termoflores', ['FLORES IV', 'FLORES1'], ['FLORES1', 'FLORES4B']], ['T2', 'BARRANQUILLA', 'Termobarranquilla', ['TEBSA'], ['BARRANQUILLA3', 'BARRANQUILLA4', 'TEBSAB']], ['T3', 'GUAJIRA', 'Termoguajira', ['GUAJIR11', 'GUAJIR21'], ['GUAJIRA1', 'GUAJIRA2']], ['T4', 'TASAJERO', 'Termotasajero', ['TASAJER1', 'TASAJERO2'], ['TASAJERO1', 'TASAJERO2']], ['T5', 'TERMOSIERRAB', 'Termosierra', ['TSIERRA'], ['TERMOSIERRAB']], ['T6', 'TERMOEMCALI1', 'Termoemcali', ['TEMCALI'], ['TERMOEMCALI1']], ['T7', 'PAIPA', 'Termopaipa', ['PAIPA1', 'PAIPA2', 'PAIPA3', 'PAIPA4'], ['PAIPA1', 'PAIPA2', 'PAIPA3', 'PAIPA4']], ['T8', 'TERMOCENTROCC', 'Termocentro', ['TCENTRO1'], ['TERMOCENTROCC']], ['T9', 'ZIPAEMG', 'Termoelectrica Martin Del Corral', ['ZIPAEMG2', 'ZIPAEMG3', 'ZIPAEMG4', 'ZIPAEMG5'], ['ZIPAEMG2', 'ZIPAEMG3', 'ZIPAEMG4', 'ZIPAEMG5']], ['T10', 'CARTAGENA', 'Central Termica De Cartagena', ['CTGEMG1', 'CTGEMG2', 'CTGEMG3'], ['CARTAGENA1', 'CARTAGENA2', 'CARTAGENA3']], ['T11', 'MERILECTRICA1', 'Central Merilectric', ['MERILEC1'], ['MERILECTRICA1']], ['H1', 'LAHERRADURA', 'Central La Herradura', ['LAHERRADURA'], ['LAHERRADURA1', 'LAHERRADURA2']], ['H2', 'JAGUAS', 'Central Jaguas', ['JAGUAS'], ['JAGUAS1', 'JAGUAS2']], ['H3', 'SANCARLOS', 'Central San Carlos', ['CSANCARLOS'], ['SANCARLOS1', 'SANCARLOS2', 'SANCARLOS3', 'SANCARLOS4', 'SANCARLOS5', 'SANCARLOS6', 'SANCARLOS7', 'SANCARLOS8']], ['H4', 'SOGAMOSO', 'Hidrosogamoso', ['SOGAMOSO'], ['SOGAMOSO1', 'SOGAMOSO2', 'SOGAMOSO3']], ['H5', 'AMOYALAESPERANZA', 'Amoya La Esperanza', ['AMOYA'], ['AMOYALAESPERANZA1', 'AMOYALAESPERANZA2']], ['H6', 'MIELI', 'Miel I', ['MIEL1'], ['MIELI1', 'MIELI2', 'MIELI3']], ['H7', 'CALDERAS', 'Calderas', ['MCALDERAS'], ['CALDERAS1', 'CALDERAS2']], ['H8', 'GUAVIO', 'Guavio', ['GUAVIO', 'MGUAVIO'], ['GUAVIO1', 'GUAVIO2', 'GUAVIO3', 'GUAVIO4', 'GUAVIO5']], ['H9', 'BETANIA', 'Represa Betania', ['BETANIA'], ['BETANIA1', 'BETANIA2', 'BETANIA3']], ['H10', 'ELQUIMBO', 'El Quimbo', ['ELQUIMBO'], ['ELQUIMBO1', 'ELQUIMBO2']], ['H11', 'PARAISO', 'Paraiso', ['PAGUA'], ['PARAISO1', 'PARAISO2', 'PARAISO3']], ['H12', 'LAGUACA', 'Guaca', ['PAGUA'], ['LAGUACA1', 'LAGUACA2', 'LAGUACA3']], ['H13', 'TEQUENDAMA', 'Tequendama', ['MB_TEQUENDA', 'MTEQUEND1', 'MTEQUEND2', 'MTEQUEND3', 'MTEQUEND4'], ['TEQUENDAMA1', 'TEQUENDAMA2', 'TEQUENDAMA3', 'TEQUENDAMA4']], ['H14', 'LATASAJERA', 'La Tasajera', ['LATASAJERA'], ['LATASAJERA1', 'LATASAJERA2', 'LATASAJERA3']], ['H15', 'CARACOLI', 'Caracoli', ['MCARACOLI'], ['CARACOLI']], ['H16', 'ELLIMONAR', 'Limonar', ['MLIMONAR'], ['ELLIMONAR']], ['H17', 'DARIOVALENCIASAMPER', 'Dario Valencia', ['DARIOVS'], ['DARIOVALENCIASAMPER1', 'DARIOVALENCIASAMPER2', 'DARIOVALENCIASAMPER5']], ['H18', 'LAGUNETA', 'Laguneta', ['MLAGUNETA'], ['LAGUNETA']], ['H19', 'PAJARITO', 'Minicentral Pajarito', ['MPAJARITO'], ['PAJARITO1', 'PAJARITO2']], ['H20', 'SANJOSEDELAMONTANA', 'Mincentral Central San Jose De La Montaña', ['MSNJOSE_MONT'], ['SANJOSEDELAMONTAÑA', 'SANJOSEDELAMONTAÑAII1']], ['H21', 'TRONERAS', 'Troneras', ['GUATRON'], ['TRONERAS1', 'TRONERAS2']], ['H22', 'GUADALUPE3', 'Guadalupe Iii', [], ['GUADALUPE31', 'GUADALUPE32', 'GUADALUPE33', 'GUADALUPE34', 'GUADALUPE35', 'GUADALUPE36']], ['H23', 'GUADALUPE4', 'Guadalupe Iv', [], ['GUADALUPE41', 'GUADALUPE42', 'GUADALUPE43']], ['H24', 'PORCEII', 'Porce Iii', ['PORCE2'], ['PORCEII1', 'PORCEII2', 'PORCEII3']], ['H25', 'PORCEIII', 'Porce Iii', ['PORCE3'], ['PORCEIII4', 'PORCEIII3', 'PORCEIII2', 'PORCEIII1']], ['H26', 'GUATAPE', 'Guatape', ['GUATAPE'], ['GUATAPE1', 'GUATAPE2', 'GUATAPE3', 'GUATAPE4', 'GUATAPE5', 'GUATAPE6', 'GUATAPE7', 'GUATAPE8']], ['H27', 'RIOABAJO', 'Rio Abajo', [], []], ['H28', 'SONSON', 'Sonson', ['MSONSON'], ['SONSON']], ['H29', 'RIOFRIO(TAMESIS)', 'Tamesis', ['MRFRIOTAMES', 'MRIOFRIO1', 'RIOFRIO2'], ['RIOFRIO\\(TAMESIS\\)']], ['H30', 'AYURA', 'Ayura', ['M_AYURA'], ['AYURA']], ['H31', 'NIQUIA', 'Niquia', ['MNIQUIA'], ['NIQUIA']], ['H32', 'URRA1', 'Urra I', ['URRA'], ['URRA1']], ['H33', 'CHIVOR', 'Chivor', ['CHIVOR'], ['CHIVOR1', 'CHIVOR2', 'CHIVOR3', 'CHIVOR4', 'CHIVOR5', 'CHIVOR6', 'CHIVOR7', 'CHIVOR8']], ['H34', 'CUCUANA', 'Cucuana', ['CUCUANA'], ['CUCUANA1', 'CUCUANA2']], ['H35', 'CALIMA', 'Calima', ['CALIMA1'], ['CALIMA1', 'CALIMA2', 'CALIMA3', 'CALIMA4']]]
CentralesOrder = ['E1','T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','H14','H15','H16','H17','H18','H19','H20','H21','H22','H23','H24','H25','H26','H27','H28','H29','H30','H31','H32','H33','H34','H35'];

Centrales = []

# Initialize
def initialize():
    for c in range(0,len(CentralesRaw)):
        temp = Central(CentralesRaw[c][0], CentralesRaw[c][1], CentralesRaw[c][2], CentralesRaw[c][3], CentralesRaw[c][4], c)
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
        toReturn = [None, None]
        if dataDN.find("ERROR DATAGET") != -1:
            toReturn[0] = dataDN
        if dataOI.find("ERROR DATAGET") != -1:
            toReturn[1] = dataOI

        return [False,toReturn] # Means there was an error

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