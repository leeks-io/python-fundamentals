# collecting_user_input.py
num_a = float(input("Enter the first number: "))
num_b = float(input("Enter the second number: "))

# printing_all_arithmetic_operations
print(f"\n{'Operation':<20}{'Result':<20}")
print("-" * 32)

print(f"{f'{num_a} + {num_b}':<20}{num_a + num_b}")
print(f"{f'{num_a} - {num_b}':<20}{num_a - num_b}")
print(f"{f'{num_a} * {num_b}':<20}{num_a * num_b}")
print(f"{f'{num_a} / {num_b}':<20}{num_a / num_b}")
print(f"{f'{num_a} // {num_b}':<20}{num_a // num_b}")
print(f"{f'{num_a} % {num_b}':<20}{num_a % num_b}")
print(f"{f'{num_a} ** {num_b}':<20}{num_a ** num_b}")


word = input("Enter a word: ")
reversed_word = word[::-1]

print(f"\nOriginal: {word}")
print(f"Reversed: {reversed_word}")
print(f"Uppercase: {reversed_word.upper()}")
print(f"length: {len(word)} characters")
print(f"Original_Uppercase: {word.upper()}")
