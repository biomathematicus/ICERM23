import  numpy as np
import  csv
from    itertools import compress

def funCSVCol(sFile, sColumn):
    with open(sFile, 'r', encoding='cp1252') as file:
        reader = csv.DictReader(file)
        if sColumn in reader.fieldnames:
            return [row[sColumn] for row in reader]
        else:
            return None
        
def extract_columns(csv_file, column_names, numeric_columns):
    data = []
    with open(csv_file, 'r', encoding='cp1252') as file:
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
    with open(sFile, encoding='cp1252') as oFile:
        next(oFile)
        for s in oFile:
            l = funStr2Lst(s) 
            out.append(l[nCol])   
    if bNum: 
        out = [int(x) for x in out]
    return out    

def funHeader(sFile):
    f = open(sFile, "r", encoding='cp1252')
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
