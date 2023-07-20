import  sys
import  numpy as np
import  matplotlib.pyplot as plt
import  csv
from    itertools import compress
# add function folder
sys.path.append('./function')
from repoExplorer import funCSVCol, funFile2Lst, funGetSublist

sFile = './data/2017-18-crdc-data/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Algebra I.csv'
cVar = ['LEA_STATE',
'LEA_STATE_NAME',
'LEAID',
'LEA_NAME',
'SCHID',
'SCH_NAME',
'COMBOKEY',
'TOT_ALGENR_GS0910_M',
'TOT_ALGENR_GS0910_F']
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
idxLargeMale = mMale > 750
idxLargeFemale = mFemale > 750

# See results 
print('Female: ', sum(mFemale[idxF]))
print('Male  : ', sum(mMale[idxM]))
# print('Schools with males in Alg II  : ', sum(idxM))
# print('Schools with females in Alg II: ', sum(idxF))
# print('States with large Alg II MALE enrollment: ',funGetSublist(idxLargeMale, cState))
# print('Districts with large Alg II MALE enrollment: ',funGetSublist(idxLargeMale, cDistrict))
# print('School with large Alg II MALE enrollment: ',funGetSublist(idxLargeMale, cSchool))
# print('States with large Alg II FEMALE enrollment: ',funGetSublist(idxLargeMale, cState))
# print('Districts with large Alg II FEMALE enrollment: ',funGetSublist(idxLargeMale, cDistrict))
# print('School with large Alg II FEMALE enrollment: ',funGetSublist(idxLargeMale, cSchool))

# Visualize results
plt.figure(1)
plt.hist(mMale[idxM], 50)
plt.xlabel('Number of Male 9th/10th-Grade Algebra 1 Students')
plt.ylabel('Number of Schools')
plt.title('Number of Male 9th/10th-Grade Students Enrolled in Algebra 1')
plt.savefig('./figure/algenrlG0910Male.png')

plt.figure(2)
plt.hist(mFemale[idxF], 50)
plt.xlabel('Number of Female 9th/10th-Grade Algebra 1 Students')
plt.ylabel('Number of Schools')
plt.title('Number of Female 9th/10th-Grade Students Enrolled in Algebra 1')
plt.savefig('./figure/algenrlG0910Female.png')
print('stop')