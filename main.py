
def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice():
    choice = input("Your choice: ")

    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return -1


def main():
    count = 0
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count = count + 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
            break
        elif choice != -1:
            print("Unknown option!")

        print()

    print("Program ending.")

main()
