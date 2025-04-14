def get_last_element(lst):
    print(lst[-1])

def main():
    lst = []
    num = int(input("Enter the number of elements in the list: "))
    for _ in range(num):
        item = input("Enter an element or number: ")
        lst.append(item)
    get_last_element(lst)

if __name__ == '__main__':
    main()
