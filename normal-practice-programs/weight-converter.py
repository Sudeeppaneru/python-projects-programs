# The program converts kilogram into lbs and vice-versa
try:
    weight = float(input("Enter the weight: "))
    unit = input("Enter kilogram or pounds(k or p): ")
    unit.lower()
    if unit == "k":
        weight = weight * 2.205
        unit = "lbs"
    elif unit == "p":
        weight = weight / 2.205
        unit = "k"
    else:
        print("please enter a valid unit")
        exit()
    print(f"After conversion the result is :{weight} {unit}")
except (ValueError, TypeError):
    print("Please enter correct data")