import json, os, glob, re

poems = []

path = os.getcwd() + '\\poems\\'

files = glob.glob(path + '*')

for i in files:
    f = open(i)
    file = f.read()

    name_pattern = re.findall(r"<author>(.+)</author>", file)
    text_pattern = re.findall(r"<text>(.*)</text>", file, flags=re.DOTALL)

    poem = {'name': name_pattern, 'text': text_pattern}
    poems.append(poem)

    f.close()

with open('poems.json', 'w') as f:
    json.dump(poems, f, indent=2)

