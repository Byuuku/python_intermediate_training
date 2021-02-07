from exercises import case_1, case_2, case_3, case_4, case_4a, case_6, case_7, case_7a


def main():
    # print("Start up c1")
    # case_1()
    # print("Finish c1")

    # print("Start up c2")
    # try:
    #     case_2("")
    # except ValueError as ve:
    #     print(f"M2 - Value exception: {ve.args} caught")
    # print("Finish c2")

    # print("Start up c3")
    # result = case_3(3, 0)
    # print(result)
    # print(f"Finish c3")

    # dictionary = {
    #     "products": ["Butter, Bread"]
    # }
    # case_4(dictionary)
    #
    # case_4a(dictionary)

    # try:
    #     case_6()
    # except NotImplementedError as not_imp_exc:
    #     print(f"Not implemented exception: {not_imp_exc.args} caught")

    case_7("file")

    case_7a()


if __name__ == "__main__":
    main()
