import json

with open('generated.json') as f:
    data = json.load(f)
    f.close()

#data = json.dumps(data, indent=2)

for i in data:
    print(i['_id'], i['company'], i['phone'])
