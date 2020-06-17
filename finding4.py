import os, fnmatch

# Take input from user and check which code he is looking for.
code = input("Which software release are you looking for? (Example: 12.3X48-D75, 12.1X46-D10, 15.1X49-D100)")
# created a separate file, which contains all version and create a list.
with open ('releases.txt') as releases:
    search = releases.read().splitlines()
# check if user enters wrong input and ask him to enter again.
while not search.__contains__(code):
    print("Invalid Input! please choose correct release: ")
    code = input("Example: 12.3X48-D75, 12.1X46-D10, 15.1X49-D100..etc \nPlease choose again:")

# check first 2 letter from user input in code variable.
code2 = code[0:2]
# create separate variable for different directories structure as per code versions, since they are in separate directories.
if (code2 != "17" and code2 != "18" and code2 != "19" and code2 != "20"):
    DIR = f'/volume/build/junos/{code[0:4]}/service/'
else:
    DIR = f'/volume/build/junos/{code[0:4]}/release/'

#
list = []
def other_dir():
    for other_dir in os.listdir(DIR):
        if other_dir.find(code) != -1 and other_dir.find('-S') == -1:
            list.append(other_dir)


other_dir()

DIR2 = []


device = input("Which platform you are looking for? (choose srx1k3k for SRX1400/SRX3400 || srx5000 for SRX5400,SRX5600,SRX5800 || srxsme for branch devices)")
for version_from_list in list:
    version2 = version_from_list[0:2]
    if (version2 != "17" and version2 != "18" and version2 != "19" and version2 != "20"):
        DIR2.append(f'/volume/build/junos/{version_from_list[0:4]}/service/{version_from_list}/ship')
    # DIR2 = [f'/volume/build/junos/{version[0:4]}/service/{version}/ship']
        version_dev = f"junos-{device}-{version_from_list}-*"

    else:
        DIR2 = [f'/volume/build/junos/{version_from_list[0:4]}/release/{version_from_list}/ship/']
        version_dev = f"*-{device}-{version_from_list}.*"
        # if device != "srxsme":
        #     version_dev = f"*{device}*-{version_from_list}.*"
        # else:
        #     version_dev = f"junos-{device}-{version_from_list}.*"


    fileList = []

    # Walk through directory

    for i in DIR2:
        for dName, sdName, fList in os.walk(i):
            for fileName in fList:
                # print(fileList.append(os.path.join(dName, fileName)))
                if fnmatch.fnmatch(fileName, version_dev): # Match search string
                    #fileList.append(fileName)
                    fileList.append(os.path.join(dName, fileName))


    for name in fileList:
        print(name)

