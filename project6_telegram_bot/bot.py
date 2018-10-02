import misc

token = misc.token

URL = 'https://api.telegram.org/bot' + token + '/'

#https://api.telegram.org/bot578761865:AAGZcI2iVKScMEmfTnIAMlmoDmW0lynCsyc/sendmessage?chat_id=307167190&text=hi

def getUpdates():
    url = URL + 'getupdates'

def main():
    getUpdates()

if __name__ == '__main__':
    main()