from urllib import request
import sys

url = 'http://www.vk.com/idpapashanskiy'

answer = request.urlopen(url)
print(answer)