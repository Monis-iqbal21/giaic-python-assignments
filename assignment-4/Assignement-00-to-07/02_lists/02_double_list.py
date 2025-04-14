def main():
    lst : int = [4,1,2,5,7]
    double_the_lst : int = []
    for i in range(len(lst)):
        double_the_lst.append(lst[i]*2)

    print(f'List after multiplication of each element : "{double_the_lst}"')
if __name__ == '__main__':
    main()