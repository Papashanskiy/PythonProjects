test_text = '''Поэма о трех тупорылых додиках

Было у отца три сына
Старший додик был, скатина
Средний был тупой дурак
Ну а младший блядь - мудак'''

test_char = '.'

test_array = test_text.split('\n')

print(''.center(50, test_char))
for i in test_array:
    print(i.center(50, test_char))
print(''.center(50, test_char))