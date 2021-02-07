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
