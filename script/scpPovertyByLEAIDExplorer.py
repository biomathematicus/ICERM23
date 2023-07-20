import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append('./function')
from repoExplorer import funCSVCol, funFile2Lst, funGetSublist

sFile = './data/poverty_ussd17.xls'

# db = pd.read_excel(sFile)
dFrame = pd.read_excel(sFile, sheet_name='USSD17')
dFrame.drop(dFrame.iloc[1:2,:],inplace=True,axis=0)
print(dFrame)