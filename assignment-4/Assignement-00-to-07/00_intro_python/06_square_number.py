def main():
    inputnum = float(input("\033[1m\033[3mEnter a number to square:\033[0m "))
    print(f"\033[1m\033[3mThe square of {str(inputnum)} is: \033[0m{str(inputnum**2)}")

if __name__ == '__main__':
    main()