import random

#                            i wrote this code by my own

# def main():
#     print(" ====== Dice Simulator ======")

#     print("Rolling the dice...")

#     for i in range(1,4):
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         print(f"Roll {i}st time result: 1st  dice : {dice1}, 2nd dice : {dice2}")


# if __name__ == '__main__':
#     main()

#                            i wrote this code by my own ends here






# ========== required code style in the assignment ==========

def dice_simulator():
    
    print("Rolling the dice...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return(f"result:\t1st  dice : {dice1} , \t2nd dice : {dice2}")

def main():
    print("\t====== Dice Simulator ======")
    print("first time",dice_simulator())
    print()
    print("second time ",dice_simulator())
    print()
    print("third time ",dice_simulator())


if __name__ == '__main__':
    main()