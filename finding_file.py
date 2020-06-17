import os, fnmatch

releases = ['12.3-X48-D75', '12.1', '15.1X49']
code = input("Which software release are you looking for? (Example: 12.3X48-D75, 12.1X46, 15.1X49)")
# if not list.__contains__(code):
#     print("invalid input")
#     exit(1)


# version = {'12.3X48-D75': "/volume/build/junos/12.3/service/{code}"}
# if code == "12.3X48-D75" or code ==  "12.1X46" or code == "15.1X49":
#DIR = f'/volume/build/junos/{code[0:4]}/service/{code}'
code2 = code[0:2]
if (code2 != "17" and code2 != "18" and code2 != "19" and code2 != "20"):
    DIR = f'/volume/build/junos/{code[0:4]}/service/'
# print(DIR)
#     file = f"{code}*"

else:
    DIR = f'/volume/build/junos/{code[0:4]}/release/'


def other_dir():
    for other_dir in os.listdir(DIR):
        if other_dir.find(code) != -1:
            print(other_dir)


other_dir()
version = input("Which release you are looking for?")

# junos-srxsme-12.1X47-D45.4-domestic.tgz

version2 = version[0:2]
if (version2 != "17" and version2 != "18" and version2 != "19" and version2 != "20"):
    DIR2 = [f'/volume/build/junos/{version[0:4]}/service/{version}/ship']
    device = input("Which platform you are looking for? (choose srx1k3k for SRX1400/SRX3400 || srx5000 for SRX5400,SRX5600,SRX5800 || srxsme for branch devices)")
    version_dev = f"junos-{device}-{version}-*"

else:
    DIR2 = [f'/volume/build/junos/{version[0:4]}/release/{version}/ship/']
    device = input("Which platform you are looking for? (srx5000 for SRX5400,SRX5600,SRX5800 || srxsme for branch devices || vsrx3 for VSRX3 )")
    if device != "srxsme":
        version_dev = f"*{device}*-{version}.*"
    else:
        version_dev = f"junos-{device}-{version}.*"


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


# 15.1X49          /homes/ssd-builder/ngsrx-yocto-daily/JUNOS_151_X49_DXXX_BRANCH/production/LATEST/[platform]/ship/[image type]/
# XXX = D### like D110/D111
# 17.3+ MR            /homes/ssd-builder/ngsrx-yocto-daily/JUNOS_XXX_R#_BRANCH/production/LATEST/[platform]/ship/[image type]/
# XXX = release version like 17.3/17.4/ect
# R# = release number like R1/R2/R3/ect
# 17.3+ SR            /homes/ssd-builder/ngsrx-yocto-daily/JUNOS_XXX_R#_S#BRANCH/production/LATEST/[platform]/ship/[image type]/
# XXX = release version like 17.3/17.4/ect
# R# = release number like R1/R2/ect
# S#= service release number like S1/S2
# 19.4R1 +
# See Above section titled "Production images (MR +SR)later than Junos 17.4R2/18.1R3-S1/18.2R2/18.3+"




# else:
#     print("Wrong choice, please enter correct version or look above for hints")
# dName = []
# for dirName, sdName, flist in os.walk(DIR2):
#     for sd in sdName:
#         if fnmatch.fnmatch(sd, version):
#             print(dName.append(os.path.join(dirName,sd)))
#
#     for path in dName:
#         print(path)






# enter = input("Many choices availble, which version you want?")

# release = []
# inDIR3 = f'/volume/build/junos//{enter}/'
# for dName, sdName, flist in os.walk(inDIR3):
#     for ver in flist:
#         if fnmatch.fnmatch(ver, enter):
#             release.append(os.path.join(dName,ver))
#
# for file in release:
#     print(file)
#

#==============================================
# inDIR = ['/volume/build/junos/12.3/service/12.3X48-D75/ship']
# inDIR = ['/volume/build/junos/']


# junos-srx5000-12.3X48-D75.4-domestic.tgz

# print(version)
#
# d2Name = []
#
# for d2Name, sdName, flist in os.walk(inDIR2):
#     for d2name2 in d2Name:
#         if fnmatch.fnmatch(d2name2, code):
#             d2Name.append(os.path.join(d2name2,sdName))
#
# for dname2 in d2Name:
#     print(dname2)

# inDIR = [f'/volume/build/junos/{code[0:4]}/service/{code}/ship']
# print(inDIR)
#


