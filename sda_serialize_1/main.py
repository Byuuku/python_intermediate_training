from pickle_training import pickle_write, pickle_read


def main():
    new_list = ["Butter", "Bread", "Water", "Soda"]
    pickle_write(new_list)

    list_of_strings = pickle_read()
    print(list_of_strings)


if __name__ == "__main__":
    main()
