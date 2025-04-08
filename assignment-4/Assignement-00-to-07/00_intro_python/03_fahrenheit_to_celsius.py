def main():
    userFahrenheit  : int = eval(input("Enter temperature in Fahrenheit: "))
    convertToCelcius : int = (userFahrenheit - 32) * 5.0/9.0
    print(f"\033[1m\033[3m Fahrenheit to Celcius : {convertToCelcius}C \033[0m")
if __name__ == '__main__':
    main()