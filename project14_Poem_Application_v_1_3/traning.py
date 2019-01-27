import random
import string
import csv

data = []

for i in range(10):
    rand_value = random.randint(3, 9)
    rand_value_2 = random.randint(100, 500)
    rand_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(rand_value))
    rand_text = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.whitespace)
                        for _ in range(rand_value_2))
    data.append({'name': rand_name, 'text': rand_text})

for i in range(len(data)):
    print(data[i]['name'] + ' :\n' + data[i]['text'])

with open('data.cvs', 'w', newline='') as f:
    f_writer = csv.writer(f)

    for i in len(data):
        f_writer.writerow(data[i])

    f.close()

