import numpy as np

def find_word_position(sWord, cList):
    if len(cList) == 0:
        return -1
    
    i = 0
    for sWord in cList:
        i += 1 
        if w == sWord:
            return i
    
    return -1  # Word not found


f = open('../data/2017-18-crdc-data/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Algebra II.csv', "r")
counter = 0
i = 0
for x in f:
    i = i + 1
    x = x.replace('"', '')
    x = x.rstrip('\n')
    y = x.split(',')    
    s = 'LEA_STATE_NAME'
    
    # s = "SCH_MATHENR_ALG2_HP_F"  # Word to search
    # y = ['"LEA_STATE","LEA_STATE_NAME","LEAID","LEA_NAME","SCHID","SCH_NAME","COMBOKEY","JJ","SCH_MATHCLASSES_ALG2","SCH_MATHCERT_ALG2","SCH_MATHENR_ALG2_HI_M","SCH_MATHENR_ALG2_HI_F","SCH_MATHENR_ALG2_AM_M","SCH_MATHENR_ALG2_AM_F","SCH_MATHENR_ALG2_AS_M","SCH_MATHENR_ALG2_AS_F","SCH_MATHENR_ALG2_HP_M","SCH_MATHENR_ALG2_HP_F","SCH_MATHENR_ALG2_BL_M","SCH_MATHENR_ALG2_BL_F","SCH_MATHENR_ALG2_WH_M","SCH_MATHENR_ALG2_WH_F","SCH_MATHENR_ALG2_TR_M","SCH_MATHENR_ALG2_TR_F","TOT_MATHENR_ALG2_M","TOT_MATHENR_ALG2_F","SCH_MATHENR_ALG2_LEP_M","SCH_MATHENR_ALG2_LEP_F","SCH_MATHENR_ALG2_IDEA_M","SCH_MATHENR_ALG2_IDEA_F"\n']

    position = find_word_position(s, y)
    print("Position:", position)


    #if  1==2: # x[0] == "9" and x[25:27] == "74":
    #    var1 = np.append(var1,x[13])   
    #    i = i + 1
print(i)










































'''


x = np.linspace(0,30,num=31)
print(x)


k=0;
for i in range(1,11):
    k=k+1/10;
print(k)
print(k==1)


# Year is 1969
def is1969(x):
    return  x[0] == "9"
    
# State is Texas
def isTexas(x):
    return x[25:26] == "74"
    
# State and County of Occurrence and Residence are the same.
def isResidentOfCOunty(x): 
    return x[10] == "1"
    
#State and County of Occurrence and Residence are the same, but county is different
def isResidentOfOtherCOunty(x): 
    return x[11] == "2"

# State and County of Occurrence and Residence are the same.
def nLiveBirths(x): 
    int(x[60:62])
    
    



    if  is1969(x) and isTexas(x) and\
        (isResidentOfCOunty(x) or isResidentOfOtherCOunty(x))\
        :            
        counter = counter + nLiveBirths(x)
        counter = counter + 1
'''    