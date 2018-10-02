from urllib import request


myUrl = "http://docs.python-requests.org/en/master/"
otvet = request.urlopen(myUrl)
myText1 = otvet.readlines()
myText2 = otvet.read()

print(otvet)
print(myText2)
for i in myText1:
    print(i)

