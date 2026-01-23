def zander_size():
    length = int(input("Enter zander length (cm): "))

    if length < 42:
        print("Release the fish.")
        print("It is", 42 - length, "cm below the size limit.")
    else:
        print("The fish meets the size limit.")


zander_size()
