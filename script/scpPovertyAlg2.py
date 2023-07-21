import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
sys.path.append('./function')
sys.path.append('./class')
from clsLEA import clsLEA 
from repoExplorer import funCSVCol, funFile2Lst, funGetSublist, funDict

## Import poverty data by LEAID
sFile = './data/poverty_ussd17.xls'

dFrame = pd.read_excel(sFile, sheet_name=0).tail(-2)
vNames = ['STATE_POSTAL', 'STATE_FIPS', 'DIST_ID', 'DIST_NAME', 'EST_POP', 'EST_POP0517', 'EST_POV_POP0517']
dFrame.columns = vNames

#LEA_ID is STATE_FIPS concatenated with DIST_ID
lLeaids = np.core.defchararray.add(dFrame['STATE_FIPS'].tolist(),dFrame['DIST_ID'].tolist())
dPoverty = dict(zip(lLeaids,dFrame['EST_POV_POP0517'].tolist()))

## Import LEA characteristics data
# oLEA = clsLEA()

## Import Algebra 2 enrollment data
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
cLEAID = cData[2]
cDistrict = cData[3]
cSchool = cData[5]
mMale = np.array(cData[7])
mFemale = np.array(cData[8])
mTotal = np.add(mMale,mFemale)

dAlg2, iMissing = funDict(cLEAID,mTotal)

## Scatter plot 1: Total district enrollment v Alg II enrollment (oLEA v dAlg2)
# xOne = []
# yOne = []
# for l in oLEA.keys():
#     if l in dAlg2.keys():
#         xOne.append(oLEA.dEnrolment[l])
#         yOne.append(dAlg2[l])
# plt.figure(1)
# plt.scatter(xOne,yOne)


## Scatter plot 2: Number of students in poverty v Alg II enrollment (lLeaids v dAlg2)
xTwo = []
yTwo = []
for l in dPoverty.keys():
    if l in dAlg2.keys():
        xTwo.append(dPoverty[l])
        yTwo.append(dAlg2[l])
plt.figure(2)
plt.scatter(xTwo,yTwo)
plt.xlabel('Number of kids ages 5-17 in poverty')
plt.ylabel('Number of students enrolled in Algebra II')
plt.title('Students in Poverty v Students Enrolled in Algebra II by District')
plt.plot([0,70000],[0,70000], color='k')
plt.savefig('./figure/figScatterPovertyAlg2.png')
