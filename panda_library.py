# Panda library is good for sorting etc or read CSV files

# import re
# regex = re.compile(r'[a-z][A-Z]/usr/')
# # r = if you want to treat it like string laterl. In windows uses \ which is problem for linux.
#
# x = regex.search('hEllo')

# read documentation in python for re module.

# match = x.group()
# print(match)
#
# find_all = regex.findall('aZllo zZtesx')
# print(find_all)
import re
list = ['19.4R2', '19.4R2-images', '19.4R2-centos', '19.4R2.1', '19.4R2.1-images', '19.4R2.2', '19.4R2.2-images', '19.4R2.3', '19.4R2.3-images', '19.4R2.4', '19.4R2.4-images', '19.4R2.5', '19.4R2.5-images', '19.4R2.6', '19.4R2.6-images', '19.4R2.6-centos']

hosts = open ('releases.txt')
content = hosts.read()
#print(content)
# print(hosts.tell())
regex = re.compile(r'12.3X48')
x = regex.search('19.4R{2}$')
print(x.group())
