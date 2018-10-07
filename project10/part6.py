str_test = 'fjsdnsfigudfjdhgliehwabcdeflkgnerlghwewelgwengwleirjwehtlweijwelfinglkdajlfkjaqj'

what_find = 'abcdef'
cash = ''
help_var = 0
for i in range(len(str_test)):
    for j in range(len(what_find)):
        if str_test[i+help_var] == what_find[j]:
            help_var += 1
            cash += str_test[i+help_var]
            print(cash)
        else:
            help_var = 0
            cash = ''
            break
    if cash == what_find:
        break