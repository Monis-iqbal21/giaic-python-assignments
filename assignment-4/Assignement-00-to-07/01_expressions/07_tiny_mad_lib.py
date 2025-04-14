ST_SENTENCE = "I am trying my best to become a better and"

def main():
    noun: str = input("Please enter a noun: ")
    verb: str = input("Please enter a verb: ")  
    adj: str = input("Please enter an adjective: ")
    print(f"\033[1m\033[3m{ST_SENTENCE} {noun} {verb} {adj}.\033[0m")

if __name__ == '__main__':
    main()