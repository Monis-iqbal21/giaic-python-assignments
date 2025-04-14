max_len: int = 3
def shorten(lst):
    while len(lst) > max_len:
        popping = lst.pop()
        print("After popping the last element: ", popping)

def lst_get():
    lst = []
    input_value = input("Enter a elements in the list: ")
    while input_value:
        lst.append(input_value)
        input_value = input("Enter a elements in the list: ")
    return lst


def main():
    shorten(lst_get())
if __name__ == '__main__':
    main()