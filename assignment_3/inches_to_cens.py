while True:
    inches = float(input("Enter inches (negative value to quit): "))
    if inches < 0:
        break
    cm = inches * 2.54
    print(f"{inches} inches is {cm:.2f} cm")