def add(num_list):
    added_numbers = 0
    for i in range(len(num_list)):
        added_numbers += num_list[i]
    return added_numbers
        
def main():
    num_count = int(input("Enter the numbers length : "))
    num_list = []
    for i in range(num_count):
        num_list.append(int(input("Please enter a number: ")))
    print(f"numbers : {num_list}")
    print(f"The sum of the numbers is {add(num_list)}")
    
if __name__ == '__main__':
    main()