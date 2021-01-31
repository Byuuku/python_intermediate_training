from cat import Cat


def main():
    cat_object = Cat("Bonifacy")
    cat_sound: str = cat_object.make_sound()
    print(cat_sound)


if __name__ == "__main__":
    main()
