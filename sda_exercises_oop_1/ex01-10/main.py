from cat import Cat


def main():
    cat_object = Cat("Bonifacy")
    cat_object_2 = Cat("Doodley", "mrrr, mrrr")
    cat_object_3 = Cat("Mruczyslaw")
    cat_object_4 = Cat("Dandy")

    cats = [cat_object, cat_object_2, cat_object_3, cat_object_4]

    for cat in cats:
        cat_sound = cat.make_sound()
        print(cat_sound)


if __name__ == "__main__":
    main()
