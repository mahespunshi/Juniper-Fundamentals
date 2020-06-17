import os, fnmatch

file = input("Enter which file are you looking for?")
file2 = f"{file}*"
inDIR2 = f'/Users/maheshkumar/PycharmProjects/Juniper-Fundamentals/{file2}'
d2Name = []


for dName, sdName, flist in os.walk(inDIR2):
    for sd in sdName:
        if fnmatch.fnmatch(sd, file2):
            d2Name.append(os.path.join(dName,sd))

for sdname2 in d2Name:
    if len(sdname2) == 0:
        print("Didn't find!")
    print(sdname2)



# enter = input("Which version you want?")
# d3Name = []
# inDIR3 = f'/Users/maheshkumar/PycharmProjects/Juniper-Fundamentals/{enter}/'
# for dName, sdName, flist in os.walk(inDIR3):
#     for ver in flist:
#         if fnmatch.fnmatch(ver, enter):
#             d3Name.append(os.path.join(dName,ver))
#
# for file in d3Name:
#     print(file)


