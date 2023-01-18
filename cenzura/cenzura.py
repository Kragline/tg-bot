import json

arr = []

with open('cenzura/cenz.txt', encoding='utf-8') as f:
    for i in f:
        word = i.lower().split('\n')[0]
        print(word)

with open('cenzura/cenz.json', 'w', encoding='utf-8') as j:
    json.dump(arr, j, indent=4)
    print('Process finished successfully')