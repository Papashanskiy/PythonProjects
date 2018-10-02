from urllib import request
import sys

url = "http://docs.python-requests.org/en/master/"
myHeader = {}
myHeader['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

req = request.Request(url, headers=myHeader)
answer = request.urlopen(req)
text = answer.readlines()

f = open('text.txt', 'w')
f.close()

f = open('text.txt', 'a')
for line in text:
    f.write(str(line)+'\n')
f.close()