from exercises import case_1, case_2


def main():
    # print("Start up c1")
    # case_1()
    # print("Finish c1")

    print("Start up c2")
    try:
        case_2("")
    except ValueError as ve:
        print(f"M2 - Value exception: {ve.args} caught")
    print("Finish c2")


if __name__ == "__main__":
    main()
