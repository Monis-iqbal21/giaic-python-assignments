def main():
    anton : int = 21
    beth : int = 6 + anton
    chen : int = 20 + beth
    drew  : int= chen + anton
    ethan : int = chen

    print(f"Anton is {str(anton)} years old")
    print(f"Beth is {str(beth)} years old")
    print(f"Chen is {str(chen)} years old")
    print(f"Drew is {str(drew)} years old")
    print(f"Ethan is {str(ethan)} years old")

if __name__ == '__main__':
    main()