import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append('./function')
from repoExplorer import funCSVCol, funFile2Lst, funGetSublist

sFile = './data/poverty_ussd17.xls'

dFrame = pd.read_excel(sFile, sheet_name=0).tail(-2)
vNames = ['STATE_POSTAL', 'STATE_FIPS', 'DIST_ID', 'DIST_NAME', 'EST_POP', 'EST_POP0517', 'EST_POV_POP0517']
dFrame.columns = vNames

#LEA_ID is STATE_FIPS concatenated with DIST_ID
lLeaids = np.core.defchararray.add(dFrame['STATE_FIPS'].tolist(),dFrame['DIST_ID'].tolist())

#Histogram generate (not very illuminating)
plt.figure(1)
plt.hist(dFrame['EST_POV_POP0517'].tolist(), 50)
plt.xlabel('Number of Children 5-17 in Poverty')
plt.ylabel('Number of School Districts')
plt.title('Number of Children in Poverty by School District')
plt.savefig('./figure/childPovertyDistrictHist.png')



print('Complete.\n')

