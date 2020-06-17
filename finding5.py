import os, fnmatch, getpass

# Take input from user and check which code he is looking for.
code = input("Which software release are you looking for? (Example: 15.1X49-D100, 17.4R1, 18.4R1, 19.4R1, 20.1R1-S1)")

code2 = code[0:2]

# created a separate file, which contains all version and create a list.
with open ('/homes/maheshkumar/releases2.txt') as releases:
    search = releases.read().splitlines()
# check if user enters wrong input and ask him to enter again.
while not search.__contains__(code) or code == '':
    print("Invalid Input! please choose correct release: ")
    code = input("Example: 15.1X49-D100, 17.4R1, 18.4R1, 19.4R1, 20.1R1-S1, 19.3R2-S3..etc ..Please choose again:")

device = input("Which platform you are looking for (srx4100, srx4200, srx1500, vsrx2, srx4600)? ")
while device != "srx4100" and device != "srx1500" and device != "vsrx2" and device != "srx4600" and device != "srx-700e" and device!= "srx4200" and device != "srx5000-RE3":
    device = input("Please enter correct device name: ")


def Dir_Walk(DIR, version_dev):
    list = []
    for dName, sdName, fList in os.walk(DIR):
        for fileName in fList:
            if fnmatch.fnmatch(fileName, version_dev): # Match search string
                list.append(os.path.join(dName, fileName))
    return list


device_Dict = {'srx'}
if code2 =="15":
    code_manipulate = f'JUNOS_{code2}1_X49_D{code[9:]}_BRANCH'
elif code.find("-S") != -1:
    code_manipulate = f'JUNOS_{code2}{code[3]}_{code[4:6]}_{code[7:]}_BRANCH'
else:
    code_manipulate = f'JUNOS_{code2}{code[3]}_{code[4:]}_BRANCH'

above_19_4 = float(code[0:4])
totalCount = 0


if above_19_4 >= 19.4:
    device_dict2 = {'srx4100': 'junos-srxmr-x86-64', 'srx4200': 'junos-srxmr-x86-64', 'vsrx2': 'junos-vsrx-x86-64', 'srx4600': 'junos-srxhe-x86-64', 'srx1500': 'junos-srxentedge-x86-64', 'srx5000-RE3': 'junos-vmhost-install-x86-64-'}
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

    result =[]
    for i in list:
        result.append(Dir_Walk(i, version_dev))

    path = ''
    for path in result[-1]:
        print(path)
    # scp(path)



    totalCount+=len(result)

else:
    device_dict = {'srx4100': 'srx-mr', 'srx4200': 'srx-mr', 'vsrx2': 'srx-mr', 'srx4600': 'srx-summit', 'srx1500': 'srx-700e'}
    device_val = device_dict.get(device)
    DIR2 = f'/homes/ssd-builder/ngsrx-yocto-daily/{code_manipulate}/production/LATEST/{device_val}/ship/cli'
    if above_19_4 == 15.1:
        version_dev2 = '*.tgz'
        file = Dir_Walk(DIR2, version_dev2)
        found = ""
        for found in file:
            print(found)
            if device == "vsrx2":
                print("\nNote: 'srxmr' .tgz upgrade images can be used to upgrade vSRX 2.0 as well (besides SRX4100/4200). Reason is that vSRX upgrade image is the same file as 'srxmr' image, just renamed to 'vsrx' before posting.")
            # scp(found)

        totalCount+=len(file)



    else:
        version_dev2 = '*.tgz'
        file = Dir_Walk(DIR2, version_dev2)
        for found in file:
            if found.find("-x86-64") != -1:
                print(found)
                scp(found)


        if device == "vsrx2":
            print("\nNote: 'srxmr' .tgz upgrade images can be used to upgrade vSRX 2.0 as well (besides SRX4100/4200). Reason is that vSRX upgrade image is the same file as 'srxmr' image, just renamed to 'vsrx' before posting.")

        totalCount+=len(file)

if totalCount == 0:
    print("Sorry not found, please confirm device and code you are looking for is correct or visit page - https://junipernetworks.sharepoint.com/teams/CSS/jtac-srx/SitePages/Process.aspx")
