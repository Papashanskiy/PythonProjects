import json

def find_poem(name):
    pass

with open('poems.json') as f:
    poems = json.load(f)

for i in poems:
    if 'O Captain! My Captain! by Walt Whitman' in i['name']:
        print(i['text'])
