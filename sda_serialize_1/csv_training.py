import csv


def csv_write(users_list):
    print("csv_write Start")
    try:
        with open("./users.csv", "a") as fd:
            writer = csv.writer(fd)
            for user_tuple in users_list:
                writer.writerow(user_tuple)

    except (IOError, Exception) as e:
        print(f"Exception while writing CSV format info {e.args}")
    print("csv_write Finish")


def csv_read():
    users_list = []
    print("csv_read Start")
    try:
        with open("./users.csv", "r") as fd:
            reader = csv.reader(fd)
            for row in reader:
                if row:
                    users_list.append(row)
    except (IOError, Exception) as e:
        print(f"Exception while reading CSV format info {e.args}")
    print("csv_read Finish")
    return users_list
