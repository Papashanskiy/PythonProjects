import random
import string
import time

PRO_LENGTH = 1000
time_start = time.time()

def string_gen(length = 10):
    str_f = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return str_f

str_test = string_gen(PRO_LENGTH)

counter = 0
while(not ('abcdef' in str_test)):
    print(str_test)
    str_test = string_gen(PRO_LENGTH)
    counter += 1

print(counter)

print('\n\n_____ %s seconds _____'% (time.time() - time_start))