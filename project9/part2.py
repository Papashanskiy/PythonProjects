from urllib import request, parse
import sys

URL = "http://google.com/search?"
value = {'q': 'Pink Floyd'}

try:
    mydata = parse.urlencode(value)
    print(mydata)
    URL =+ mydata
    req = request.Request(URL)
    answer = request.urlopen(req)
    answer = answer.readlines()
    for i in answer:
        print(i)
except Exception:
    print("Что-то пошло не так")
    print(sys.exc_info()[1])