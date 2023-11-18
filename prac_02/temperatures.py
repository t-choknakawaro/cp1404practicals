MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Get fahrenheit and celsius and convert them to another degree"""
    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'C':
            celsius = float(input('Celsius: '))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f'Result: {fahrenheit:.2f} F')
        elif choice == 'F':
            fahrenheit = float(input('Fahrenheit: '))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f'Result: {celsius:.2f} C')
        else:
            print('Invalid option')
        print(MENU)
        choice = input('>>> ').upper()
    print('Thank you.')


def convert_celsius_to_fahrenheit(celsius):
    """Convert the input celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert the input fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()

# """
# CP1404/CP5632 - Practical
# Pseudocode for temperature conversion
# """
#
# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print(f"Result: {fahrenheit:.2f} F")
#     elif choice == "F":
#         fahrenheit = float(input('Fahrenheit: '))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print(f'Result: {celsius:.2f}')
#         # Hint: celsius = 5 / 9 * (fahrenheit - 32)
#         # Remove the "pass" statement when you are done. It's a placeholder.
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")
