import  sys
# add function folder
sys.path.append('./function')
from repoExplorer import funCSVCol, funFile2Lst, funGetSublist
class clsLEA:
    def __init__(self):
        # Define c=variables from CSV
        sFile = './data/2017-18-crdc-data/2017-18 Public-Use Files/Data/LEA/CRDC/CSV/LEA Characteristics.csv'
        cVar = ['LEA_STATE',
        'LEA_STATE_NAME',
        'LEAID',
        'LEA_NAME',
        'LEA_ADDRESS',
        'LEA_CITY',
        'LEA_ZIP',
        'LEA_ENR',
        'LEA_SCHOOLS']
        # Mark numeric fields with 1
        cNumType = [0,0,0,0,0,0,0,1,1]
        # Laod the file incoa list of columns
        self.cLEA = funFile2Lst(cVar, cNumType, sFile)
        # Extract variables that will be used
        cState = self.cLEA[1]
        cLEAID = self.cLEA[2]
        cNumEnr = self.cLEA[7]
        cNumSchool = self.cLEA[8]
        #Overkill: Dtaa dictionaries per variable
        self.dState = dict(zip(cLEAID,cState))
        self.dNmbrSchool = dict(zip(cLEAID,cNumSchool))
        self.dEnrolment = dict(zip(cLEAID,cNumEnr))      

        