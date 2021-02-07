from pickle_training import pickle_write, pickle_read
from csv_training import csv_write


def main():
    # new_list = ["Butter", "Bread", "Water", "Soda"]
    # pickle_write(new_list)
    #
    # list_of_strings = pickle_read()
    # print(list_of_strings)

    new_users = [
        ("John", "Smith", 93121323542),
        ("Gary", "Youngman", 99062090756),
        ("Agatha", "Brown", 88061245692)
    ]

    csv_write(new_users)


if __name__ == "__main__":
    main()
