import random

def main():
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)
    total: int = dice1 + dice2
    print(f'dice 1 : "{dice1}" and dice 2 : "{dice2}"')
    print(f'Your total from dice 1 and 2 is {total}.')

if __name__ == '__main__':
    main()
