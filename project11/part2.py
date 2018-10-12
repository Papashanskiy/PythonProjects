test_text = '''Поэма о трех тупорылых додиках

Было у отца три сына
Старший додик был, скатина
Средний был тупой дурак
Ну а младший блядь - мудак'''

test_array = test_text.split('\n')

for i in range(len(test_array)):
    print(str(i+1) + test_array[i].center(40, ' '))