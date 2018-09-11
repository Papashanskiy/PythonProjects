def max(arr):
    m = arr[0]
    for i in arr:
        if m < i:
            m = i
    return m

def myCount(arr):
    count = 0
    for i in arr:
        count += 1
    return count

def dElement(arr):
    i = 0
    while i < (myCount(arr)):
        print(arr[i])
        i += 1
    pass

def exportFromFile():
    f = open('file.txt', 'r')
    arr = list()
    for i in f:
        arr.append(i)
    f.close()
    return arr

def importToFile(str):
    f = open('file.txt', 'a')
    f.write(str + "\n")
    f.close()
    pass

def delDataInFile():
    f = open('file.txt', 'w')
    f.write("")
    f.close()
    pass

def listToStr(arr):
    str = ""
    for i in arr:
        str += i
    return str

def rec(n):
    if n > -1:
        print(n, " ")
        return rec(n-1)

def strToList(str):
    arr = []
    n = ""
    for i in str:
        if i != " ":
            n += i
            print(str.index(i), " ", len(str))
        elif n != '':
            arr.append(n)
            n = ""
    if n != "":
        arr.append(n)
    return arr

def longStrToDoubleArray(str):
    arr = str.split('\n')
    for i in arr:
        arr[arr.index(i)] = i.split()
    return arr

def startingList():
    arr = [1, 2, 64, 46, 882, 63, 23, 36, 63, 36, 84, 3, 882, 23, 10]
    return arr

def startingString():
    str = "a b c dddd e fffff"
    return str