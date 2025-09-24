# function with return values
#Each function performs a calculation and uses returns result back to the main program to be displayed.

# Converts Celsius to Fahrenheit and returns result
def cel_to_fah(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

# Converts Fahrenheit to Celsius and returns result
def fah_to_cel(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius

# Converts Celsius to Kelvin and returns result
def cel_to_kel(celsius):
    kelvin=celsius+273.15
    return kelvin

# Converts Kelvin to Celsius and returns result
def kel_to_cel(kelvin):
    celsius=kelvin-273.15
    return celsius

def main():
    print("🌡️ TEMPERATURE CONVERTER")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    try:
        choice=input("Enter your choice(1-4) : ")

        if choice in ['1','2','3','4']:
            temp=float(input("Enter temperature : "))

            if choice =='1':
                new_temp=cel_to_fah(temp)
                print(f"{temp}℃ is equal to {new_temp:.2f}℉")

            elif choice == '2':
                new_temp = fah_to_cel(temp)
                print(f"{temp}°F is equal to {new_temp:.2f}°C")

            elif choice == '3':
                new_temp = cel_to_kel(temp)
                print(f"{temp}°C is equal to {new_temp:.2f} K")

            elif choice == '4':
                new_temp = kel_to_cel(temp)
                print(f"{temp} K is equal to {new_temp:.2f}°C")

        else:
            print("Invalid choice. Please enter number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter numeric value for temperature.")

if __name__ == "__main__":
     main()