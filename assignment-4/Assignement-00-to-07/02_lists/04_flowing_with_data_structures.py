def add_three_copies(lst, data):
    for i in range(3):
        lst.append(data)


def main():
    message = input("Enter something: ")
    lst = []
    print("List before:", lst)
    add_three_copies(lst, message)
    print("List after:", lst)

if __name__ == "__main__":
    main()