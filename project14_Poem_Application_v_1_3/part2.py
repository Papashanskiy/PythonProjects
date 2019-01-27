import json
import random
import string


def rand_poem():
    name = ''.join(random.choice(string.ascii_uppercase)) + \
           ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(4, 11)))
    text = ''.join(random.choice(string.ascii_lowercase + string.whitespace) for _ in range(random.randint(500, 1000)))
    poem = {
        'name': name,
        'text': text
    }
    return poem


poems = []

for i in range(150):
    poems.append(rand_poem())

poems_json = json.dumps(poems, indent=2)

with open('poems.json', 'w') as f:
    json.dump(poems, f, indent=2)
