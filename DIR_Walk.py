import os, fnmatch

class Dir_Walk(object):


def Dir_Walk(DIR, version_dev):
    list = []
    for dName, sdName, fList in os.walk(DIR):
        for fileName in fList:
            if fnmatch.fnmatch(fileName, version_dev): # Match search string
                list.append(os.path.join(dName, fileName))
    return list[0]
