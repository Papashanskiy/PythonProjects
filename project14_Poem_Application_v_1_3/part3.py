import json

with open('poems.json') as f:
    poems = json.load(f)
    f.close()

for i in poems:
    print(len(poems))
