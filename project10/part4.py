import random
import string
import time
import os

def string_gen(str_length = 10):
    str_work = ''.join(random.choice(string.ascii_uppercase +
                                     string.digits +
                                     string.ascii_lowercase) for _ in range(str_length))
    return str_work

start = time.time()

os.chdir(r"C:\Users\Игорь\Desktop\\")

print(os.getcwd())

print('\n____ %s seconds ____'% (time.time() - start))