import  sys
import  numpy as np
import  matplotlib.pyplot as plt
import  csv
from    itertools import compress
# add function folder
sys.path.append('./function')
from repoExplorer import funCSVCol, funFile2Lst, funGetSublist

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
cLeaid = cData[2]
cDistrict = cData[3]
cSchool = cData[5]
mMale = np.array(cData[7])
mFemale = np.array(cData[8])
mTotal = np.add(mMale,mFemale) # Do we need to check for negatives here?

iMissing = 0

# Perform district-level aggregation by LEAID into dict dAlg2
dAlg2 = {}
for (k,v) in zip(cLeaid,mTotal):
    if v < 0:
        iMissing += 1
        continue
    if k in dAlg2.keys():
        dAlg2[k] += v
    else:
        dAlg2[k] = v

print(dAlg2['0100005'])
