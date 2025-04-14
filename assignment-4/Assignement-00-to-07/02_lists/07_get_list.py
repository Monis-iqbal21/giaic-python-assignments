def main():
    lst = []
    num = input("Enter the number of elements in the list: ")
    while num:
        lst.append(num)
        num= input("Enter the number of elements in the list: ")
    
    print("List : " ,lst)

if __name__ == '__main__':
    main()