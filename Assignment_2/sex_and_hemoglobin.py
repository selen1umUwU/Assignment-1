def check_hemoglobin():
    gender = input("Enter your biological sex (female/male): ").lower()
    value = float(input("Enter your hemoglobin value (g/l): "))

    if gender == "female":
        if value < 117:
            print("Hemoglobin value is low.")
        elif 117 <= value <= 155:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    elif gender == "male":
        if value < 134:
            print("Hemoglobin value is low.")
        elif 134 <= value <= 167:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    else:
        print("Invalid gender entered.")

check_hemoglobin()
