import os, fnmatch
code = input("Which software release are you looking for? (Example: 12.3X48-D75, 12.1X46-D10, 15.1X49-D100, 17.4R1, 18.4R1, 20.1R1-S1)")
code2 = code[0:2]

device = input("Which platform you are looking for (srx4100, srx4200, srx1500, vsrx2, srx4600)? ")

device_dict2 = {'srx4100': 'junos-srxmr-x86-64', 'srx4200': 'junos-srxmr-x86-64', 'vsrx2': 'junos-vsrx-x86-64', 'srx4600': 'junos-srxhe-x86-64', 'srx1500': 'junos-srxentedge-x86-64'}
device_val2 = device_dict2.get(device)
version_dev = f"{device_val2}-{code}*"

DIR = f'/volume/build/junos/{code[0:4]}/release/'
list = []
if "-S" not in code:
    for other_dir in os.listdir(DIR):
        if other_dir.find(code) != -1 and other_dir.find('-S') == -1 and other_dir.find('-images') != -1:
            list.append(os.path.join(DIR, other_dir))
elif "-S" in code:
    for other_dir in os.listdir(DIR):
        if other_dir.find(code) != -1 and other_dir.find('-images') != -1 and other_dir.find('-S') != -1:
            list.append(os.path.join(DIR, other_dir))

def Dir_Walk(DIR, version_dev):
    list = []
    for dName, sdName, fList in os.walk(DIR):
        for fileName in fList:
            if fnmatch.fnmatch(fileName, version_dev): # Match search string
                list.append(os.path.join(dName, fileName))
    return list


result =[]
for i in list:
    result.append(Dir_Walk(i, version_dev))

print(result[-1])
