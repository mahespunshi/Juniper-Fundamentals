import os, fnmatch


# Take input from user and check which code he is looking for.
code = input("Which software release are you looking for? (Example: 12.3X48-D75, 12.1X46-D10, 15.1X49-D100, 17.4R1, 18.4R1, 20.1R1-S1)")

# created a separate file, which contains all version and create a list.
with open ('releases.txt') as releases:
    search = releases.read().splitlines()
# check if user enters wrong input and ask him to enter again.
while not search.__contains__(code) or code == '':
    print("Invalid Input! please choose correct release: ")
    code = input("Example: 12.3X48-D75, 12.1X46-D10, 15.1X49-D100, 17.4R1, 18.4R1, 19.3R2-S3..etc ..Please choose again:")

# check first 2 letter from user input in code variable.
code2 = code[0:2]

# create separate variable for different directories structure as per code versions, since they are in separate directories.
if (code2 != "17" and code2 != "18" and code2 != "19" and code2 != "20"):
    list = []
    DIR = f'/volume/build/junos/{code[0:4]}/service/'
    for other_dir in os.listdir(DIR):
        if other_dir.find(code) != -1:
            list.append(other_dir)

else:

    DIR = f'/volume/build/junos/{code[0:4]}/release/'
    list = []
    if "-S" not in code:
        for other_dir in os.listdir(DIR):
            if other_dir.find(code) != -1 and other_dir.find('-S') == -1:
                list.append(other_dir)
    elif "-S" in code:
        for other_dir in os.listdir(DIR):
            if other_dir.find(code) != -1:
                list.append(other_dir)

DIR2 = []


device = input("Which platform you are looking for? (choose 'srx1k3k' for SRX1400/SRX3400/SRX3600 || 'srx5000' for SRX5400,SRX5600,SRX5800 || 'srxsme' for All SRX Branch devices || 'vsrx3' for VSRX3.0) ")
while device != "srx1k3k" and device != "srx5000" and device != "srxsme" and device != 'vsrx3' and device != 'srx5000-RE3':
    device = input("Please choose correct device name (such as 'srx1k3k' for SRX1400/SRX3400/SRX3600 || 'srx5000' for SRX5400,SRX5600,SRX5800 || 'srxsme' for All SRX Branch devices || 'vsrx3' for VSRX3.0)")

if (code2 == "17" and device == "srx1k3k") or (code2 == "18" and device == "srx1k3k") or (code2 == "19" and device == "srx1k3k") or (code2 == "20" and device == "srx1k3k"):
    print("Note: code versions 17,18,19,20 are not available for srx1k3k devices")
    exit(1)

totalCount = 0
fileList = []
for version_from_list in list:
    version2 = version_from_list[0:2]
    if (version2 != "17" and version2 != "18" and version2 != "19" and version2 != "20"):
        DIR2.append(f'/volume/build/junos/{version_from_list[0:4]}/service/{version_from_list}/ship')
        version_dev = f"junos-{device}-{version_from_list}-domestic.tgz"

    else:
        DIR2 = [f'/volume/build/junos/{version_from_list[0:4]}/release/{version_from_list}/ship/']
        if device != "srxsme":
            version_dev = f"junos-install-{device}-x86-64-{version_from_list}.tgz"
        elif device == "srx5000-RE3":
            version_dev = f"junos-vmhost-install-srx-x86-64-{version_from_list}*"
        else:
            version_dev = f"junos-{device}-{version_from_list}.tgz"




    # Walk through directory

    for i in DIR2:
        for dName, sdName, fList in os.walk(i):
            for fileName in fList:
                if fnmatch.fnmatch(fileName, version_dev): # Match search string
                    fileList.append(os.path.join(dName, fileName))



    # for name in fileList:
    #     # if name.endswith('.tgz'):
    #     print(name)
    totalCount+=len(fileList)

if totalCount == 0:
    print("Sorry not found, please confirm device and code you are looking for is correct or visit page - https://junipernetworks.sharepoint.com/teams/CSS/jtac-srx/SitePages/Process.aspx")

else:
    print(fileList[-1])
