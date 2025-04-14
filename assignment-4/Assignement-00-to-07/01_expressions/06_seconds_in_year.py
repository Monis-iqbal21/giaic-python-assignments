DAY : int = 365
HOUR : int = 24
MINUTE : int = 60
SECOND : int = 60
def main():
    sec_in_year: int = DAY * HOUR * MINUTE * SECOND
    print(f'There are "{sec_in_year}" seconds in a year.')



if __name__ == '__main__':
    main()