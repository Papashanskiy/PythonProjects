from urllib import request
import sys

webUrl = 'https://pp.userapi.com/c847020/v847020332/eedde/EoG1KBX4x8M.jpg'
fileUrl = 'C:\\Users\\Игорь\\Desktop\\Python\\MyDownloads\\pic.jpeg'

try:
    print("Downloading is started...")
    request.urlretrieve(webUrl, fileUrl)
except Exception:
    print("Warning!")
    print(sys.exc_info()[1])