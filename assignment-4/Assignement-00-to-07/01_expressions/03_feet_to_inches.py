def main():
    in_foot = float(input("Enter value in feet: ")) 
    in_inches = in_foot * 12
    print(f"\033[1m\033[3m{str(in_foot)} feet is equal to {str(in_inches)} inches\033[0m")
if __name__ == '__main__':
    main()