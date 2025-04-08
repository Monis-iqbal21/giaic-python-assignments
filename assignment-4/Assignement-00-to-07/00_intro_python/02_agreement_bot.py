def main():
    favAnimal : str = input("\033[1m\033[3mWhat's your favorite animal? : \033[0m")
    print(f"My favorite animal is also \033[1m\033[3m{favAnimal}\033[0m!")
if __name__ == '__main__':
    main()