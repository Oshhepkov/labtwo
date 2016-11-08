import re
file= open('access.log' , 'r') 
fSet=set() 
for line1 in file.readlines(): 
    result = re.findall(r'[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]' , line1)
    sSet=str(result)
    res1 = re.search(r'[2][5][6-9]', sSet)
    res2 = re.search(r'[2][6-9][0-9]', sSet)
    if (not res1 and not res2): 
        fSet.update(result) 
fSet = list(fSet)

sSet=set() 
for line2 in fSet:
    result = re.findall(r'[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.', line2) 
    sSet.update(result) 
sSet = list(sSet)
for line2 in sSet:
    for item in fSet:
        if item.startswith(line2):
            print(item)
    print(" ")
    
    

