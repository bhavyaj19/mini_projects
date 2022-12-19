import sys 
import clipboard            #modules in python
import json

saved_data="clipboard.json"

def save_items(filepath, data):
    with open(filepath,"w") as f:
        json.dump(data,f)

def load_items(filepath):
    try:
        with open(filepath,"r") as f:
            data=json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2: 
    command =sys.argv[1] 
    data=load_items(saved_data)

    if command=="save":
        key = input("Enter a key: ")
        data[key]=clipboard.paste()
        save_items(saved_data,data)


    elif command=="load":
        key=input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print('data copird to clipboard')

        else:
            print('key does not exist')

    elif command=="list":
        print(load_items(saved_data))

    else:
        print("Unknown command")
else:
    print("Enter only one command")
