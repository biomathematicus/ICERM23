import  sys
import  numpy as np
import  matplotlib.pyplot as plt
import  csv
from    itertools import compress
# add function folder
sys.path.append('./function')
import repoExplorer 

def funCSVCol(sFile, sColumn):
    with open(sFile, 'r') as file:
        reader = csv.DictReader(file)
        if sColumn in reader.fieldnames:
            return [row[sColumn] for row in reader]
        else:
            return None
        
def extract_columns(csv_file, column_names, numeric_columns):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            extracted_row = []
            for column_name in column_names:
                if column_name in numeric_columns:
                    extracted_row.append(float(row[column_name]))
                else:
                    extracted_row.append(row[column_name])
            data.append(extracted_row)
    return data
       

def funWordPos(sWord, cList):
    i = -1
    for sItem in cList:
        i += 1 
        if sItem == sWord:
            return i
    return i

def funStr2Lst(s):
    s = s.replace('"', '')
    s = s.rstrip('\n')
    l = s.split(',')   
    return l

def funColumn(nCol, bNum, sFile):
    out = []
    with open(sFile) as oFile:
        next(oFile)
        for s in oFile:
            l = funStr2Lst(s) 
            out.append(l[nCol])   
    if bNum: 
        out = [int(x) for x in out]
    return out    

def funHeader(sFile):
    f = open(sFile, "r")
    cHeader = funStr2Lst(f.read())
    f.close()
    return cHeader

def funFile2Lst(cVar, cType, sFile):
    out = []
    cHeader = funHeader(sFile)
    i = 0
    for s in cVar:
        n = funWordPos(s, cHeader)
        cCol = funColumn(n,cType[i],sFile)
        out.append(cCol)
        i += 1
    return out

def funGetSublist(idx, cList):
    pos = list(compress(range(len(idx)), idx))
    out = []
    for n in pos:
        out.append(cList[n])
    return out

sFile = './data/2017-18-crdc-data/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Algebra II.csv'
cVar = ['LEA_STATE',
'LEA_STATE_NAME',
'LEAID',
'LEA_NAME',
'SCHID',
'SCH_NAME',
'COMBOKEY',
'TOT_MATHENR_ALG2_M',
'TOT_MATHENR_ALG2_F']
cNumType = [0,0,0,0,0,0,0,1,1]

#First, using libraries courtesy of ChatGPT
#cNum = ['TOT_MATHENR_ALG2_M','TOT_MATHENR_ALG2_F']
#cData = funCSVCol(sFile, 'TOT_MATHENR_ALG2_M')
#cData = extract_columns(sFile, cVar, cNum)

# Hard-core implementation of data retrieval without libraries
cData = funFile2Lst(cVar, cNumType, sFile)

# Extract variables that will be used
cState = cData[1]
cDistrict = cData[3]
cSchool = cData[5]
mMale = np.array(cData[7])
mFemale = np.array(cData[8])

# Create indexes for filtering data
idxF = mFemale > 0
idxM = mMale > 0
idxLargeMale = mMale[idxM] > 750
idxLargeFemale = mFemale[idxF] > 750

# See reults 
print('Female: ', sum(mFemale[idxF]))
print('Male  : ', sum(mMale[idxM]))
print('Schools with males in Alg II  : ', sum(idxM))
print('Schools with females in Alg II: ', sum(idxF))
print('States with large Alg II MALE enrollment: ',funGetSublist(idxLargeMale, cState))
print('Districts with large Alg II MALE enrollment: ',funGetSublist(idxLargeMale, cDistrict))
print('School with large Alg II MALE enrollment: ',funGetSublist(idxLargeMale, cSchool))
print('States with large Alg II FEMALE enrollment: ',funGetSublist(idxLargeMale, cState))
print('Districts with large Alg II FEMALE enrollment: ',funGetSublist(idxLargeMale, cDistrict))
print('School with large Alg II FEMALE enrollment: ',funGetSublist(idxLargeMale, cSchool))

# Visualize results
plt.hist(mMale[idxM], 50)
plt.show()
plt.hist(mFemale[idxF], 50)
plt.show()
print('stop')