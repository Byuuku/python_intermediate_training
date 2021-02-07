from pickle_training import pickle_write, pickle_read
from csv_training import csv_write, csv_read
from json_training import json_write, json_read


def main():
    # new_list = ["Butter", "Bread", "Water", "Soda"]
    # pickle_write(new_list)
    #
    # list_of_strings = pickle_read()
    # print(list_of_strings)

    # new_users = [
    #     ("John", "Smith", 93121323542),
    #     ("Gary", "Youngman", 99062090756),
    #     ("Agatha", "Brown", 88061245692)
    # ]
    #
    # csv_write(new_users)
    # users_list = csv_read()
    # print(users_list)

    new_objects = [
        {
            "object": "Line",
            "points": 0,
            "lines": 1
        },
        {
            "object": "Circle",
            "points": 0,
            "lines": 1
        },
        {
            "object": "Triangle",
            "points": 3,
            "lines": 3
        },
        {
            "object": "Square",
            "points": 4,
            "lines": 3
        }
    ]

    json_write(new_objects)

    data_list = json_read()
    print(data_list)


if __name__ == "__main__":
    main()
