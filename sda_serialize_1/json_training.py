import json


def json_write(items: list):
    print("json_write Start")
    try:
        with open("./objects.json", "w") as fd:
            json.dump(items, fd, indent=2)
    except (IOError, Exception) as e:
        print(f"Exception while writing JSON format info {e.args}")
    print("json_write Finish")


def json_read():
    data_list = []
    print("json_read Start")
    try:
        with open("./objects.json", "r") as fd:
            data_list = json.load(fd)
    except (IOError, Exception) as e:
        print(f"Exception while reading JSON format info {e.args}")
    print("json_read Finish")
    return data_list
