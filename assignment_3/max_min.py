numbers = []
while True:
    user_input = input("Enter a number (empty string to quit): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

if numbers:
    print(f"Largest number: {max(numbers)}")
    print(f"Smallest number: {min(numbers)}")