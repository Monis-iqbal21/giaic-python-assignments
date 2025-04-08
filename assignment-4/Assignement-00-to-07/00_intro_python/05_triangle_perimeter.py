def main():
    first_side = float(input("\033[1m\033[3mmEnter the length of the 1st side of the triangle:\033[0m ")) 
    second_side = float(input("\033[1m\033[3mmEnter the length of the 2nd side of the triangle:\033[0m "))
    third_side = float(input("\033[1m\033[3mmEnter the length of the 3rd side of the triangle:\033[0m ")) 
    perimeter = first_side + second_side + third_side
    print(f"The perimeter of the triangle is: \033[1m\033{str(perimeter)}\033[0m")
if __name__ == '__main__':
    main()