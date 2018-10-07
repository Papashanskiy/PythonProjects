import re
import glob
import os

print(os.getcwd())

os.chdir('C:\\Users\\Игорь\\Desktop\\Python\\')
os.chdir('C:\\Users\\Игорь\\Desktop\\Python\\Notes\\Sintax\\')

arr = glob.glob('*.txt')

for i in arr:
    print(i)

f = open('ОС.txt', 'r')
str = ''
for i in f:
    str += i + '\n'
f.close()

print(str)

str3 = ''
for i in range(150):
    str3 += '*'
print(str3)

result = re.findall(r'\b[А-Яа-я]\w+', str)
for i in result:
    print(i)