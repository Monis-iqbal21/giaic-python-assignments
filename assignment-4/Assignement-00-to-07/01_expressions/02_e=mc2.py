c: int = 299792458
def main():
    mass_kg : float = float(input("\033[1m\033[3mEnter mass in kg:\033[0m "))
    e_joules : float = mass_kg * (c**2)

    print("formula: E = mc^2")
    print(f"mass: {mass_kg} kg")
    print(f"speed of light: {str(c)} m/s")
    print(f"energy: {e_joules} joules")


if __name__ == '__main__':
    main()