import pickle


def pickle_write(items: list):
    print("pickle_write Start")
    try:
        with open("./data.pickle", "wb") as fd:
            pickle.dump(items, fd)
            print(pickle.dumps(items))
    except (IOError, Exception) as e:
        print(f"Exception while writing Pickle format info {e.args}")
    print("pickle_write Finish")


def pickle_read():
    string_list = []
    print("pickle_read Start")
    try:
        with open("./data.pickle", "rb") as fd:
            string_list = pickle.load(fd)
    except (IOError, Exception) as e:
        print(f"Exception while reading Pickle format info {e.args}")
    print("pickle_read Finish")
    return string_list
