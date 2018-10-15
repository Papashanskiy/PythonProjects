import json

def binary_search(arr, search_obj):
    flag = len(arr) // 2
    if arr[flag] == search_obj:
        return flag
    elif arr[flag] > search_obj:
        binary_search(arr[flag:-1], search_obj)
    else:
        binary_search(arr[1:flag], search_obj)

f = open('data.txt', 'r')
data = json.load(f)
f.close()

print(binary_search(data['array'], 353))