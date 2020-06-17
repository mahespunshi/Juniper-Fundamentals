import os, fnmatch, getpass
os.system("stty erase '^H'")
os.system("stty erase '^?'")

def scp(variable):
    scp = input("Would you like to transfer this file to lab device? 'Yes' or 'No'>")
    while scp != 'Yes' and scp != 'No' and scp != 'yes' and scp != 'no':
        scp = input("Would you like to transfer this file to lab device? 'Yes' or 'No'>")
    if scp == 'Yes' or scp =='yes':
        hostname = input("Provide Device ip address: ")
        username = input("Provide user name: ")
        password = getpass.getpass("Provide password: ")
        print("Please wait, while copying file ..... (Note: if provided login information is incorrect, program will terminate quickly)")
        os.system(f"sshpass -p {password} scp -o StrictHostKeyChecking=no {variable} {username}@{hostname}:/var/tmp/")
        exit(0)

    else:
        print("Alright... Bye for now")

Ask = input("Are you looking for 'TVP' or 'Non-TVP' platform? TVP (SRX4k, SRX1500, VSRX2.0) and Non-TVP(SRX300, SRX500HM, SRX650, SRX1400, SRX3K, SRX5k)>")
while Ask != 'TVP' and Ask != 'tvp' and Ask != 'Non-TVP' and Ask != 'non-tvp':
    Ask = input("Are you looking for 'TVP' or 'Non-TVP' platform?>")

if Ask == "Non-TVP" or Ask == "non-tvp":
# Take input from user and check which code he is looking for.
    code = input("Which software release are you looking for? (Example: 12.3X48-D75, 12.1X46-D10, 15.1X49-D100, 17.4R1, 18.4R1, 20.1R1-S1)>")

    # created a separate file, which contains all version and create a list.
    with open ('/homes/maheshkumar/releases.txt') as releases:
        search = releases.read().splitlines()
    # check if user enters wrong input and ask him to enter again.
    while not search.__contains__(code) or code == '':
        print("Invalid Input! please choose correct release: ")
        code = input("Example: 12.3X48-D75, 12.1X46-D10, 15.1X49-D100, 17.4R1, 18.4R1, 19.3R2-S3..etc ..Please choose again:>")

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

    device = input("Which platform you are looking for? (choose 'srx1k3k' for SRX1400/SRX3400/SRX3600 || 'srx5000' for SRX5400,SRX5600,SRX5800 || 'srxsme' for All SRX Branch devices || 'vsrx3' for VSRX3.0)>")
    while device != "srx1k3k" and device != "srx5000" and device != "srxsme" and device != 'vsrx3':
        device = input("Please choose correct device name (such as 'srx1k3k' for SRX1400/SRX3400/SRX3600 || 'srx5000' for SRX5400,SRX5600,SRX5800 || 'srxsme' for All SRX Branch devices || 'vsrx3' for VSRX3.0)>")

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
            else:
                version_dev = f"junos-{device}-{version_from_list}.tgz"

        # Walk through directory
        for i in DIR2:
            for dName, sdName, fList in os.walk(i):
                for fileName in fList:
                    if fnmatch.fnmatch(fileName, version_dev): # Match search string
                        fileList.append(os.path.join(dName, fileName))

        totalCount+=len(fileList)

    if totalCount == 0:
        print("Sorry not found, please confirm device and code you are looking for is correct or visit page - https://junipernetworks.sharepoint.com/teams/CSS/jtac-srx/SitePages/Process.aspx")

    else:
        file = fileList[-1]
        print(file)
        scp(file)

else:
    code = input("Which software release are you looking for? (Example: 15.1X49-D100, 17.4R1, 18.4R1, 19.4R1, 20.1R1-S1)>")

    code2 = code[0:2]

    # created a separate file, which contains all version and create a list.
    with open ('/homes/maheshkumar/releases2.txt') as releases:
        search = releases.read().splitlines()
    # check if user enters wrong input and ask him to enter again.
    while not search.__contains__(code) or code == '':
        print("Invalid Input! please choose correct release: ")
        code = input("Example: 15.1X49-D100, 17.4R1, 18.4R1, 19.4R1, 20.1R1-S1, 19.3R2-S3..etc ..Please choose again:>")

    device = input("Which platform you are looking for (srx4100, srx4200, srx1500, vsrx2, srx4600)? >")
    while device != "srx4100" and device != "srx1500" and device != "vsrx2" and device != "srx4600" and device!= "srx4200":
        device = input("Please enter correct device name: ")


    def Dir_Walk(DIR, version_dev):
        list = []
        for dName, sdName, fList in os.walk(DIR):
            for fileName in fList:
                if fnmatch.fnmatch(fileName, version_dev): # Match search string
                    list.append(os.path.join(dName, fileName))
        return list


    #device_Dict = {'srx'}
    if code2 =="15":
        code_manipulate = f'JUNOS_{code2}1_X49_D{code[9:]}_BRANCH'
    elif code.find("-S") != -1:
        code_manipulate = f'JUNOS_{code2}{code[3]}_{code[4:6]}_{code[7:]}_BRANCH'
    else:
        code_manipulate = f'JUNOS_{code2}{code[3]}_{code[4:]}_BRANCH'

    above_19_4 = float(code[0:4])
    totalCount = 0


    if above_19_4 >= 19.4:
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

        result =[]
        for i in list:
            result.append(Dir_Walk(i, version_dev))

        path = ''
        for path in result[-1]:
            print(path)
        scp(path)



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
                scp(found)

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
