def add_numbers() -> float:
    a = float(input("Num1: "))
    b = float(input("Num2: "))
    return a + b

def rest_numbers() -> float:
    a = float(input("Num1: "))
    b = float(input("Num2: "))
    return a - b

def mult_numbers() -> float:
    a = float(input("Num1: "))
    b = float(input("Num2: "))
    return a * b

def div_numbers() -> float:
    a = float(input("Num1: "))
    b = float(input("Num2: "))
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def main():
    print("\n----------> CALCULATOR \n\n")
    operation = int(input("Choose operation (1=Add, 2=Sub, 3=Mult, 4=Div): "))

    operations = {
        1: ("Addition", add_numbers),
        2: ("Substraction", rest_numbers),
        3: ("Multiplication", mult_numbers),
        4: ("Division", div_numbers)
    }

    try:
        label, func = operations[operation]
        result = func()
        print(f"{label} result: {result}")
    except KeyError:
        raise ValueError("Operation Unknown")

if __name__ == "__main__":
    main()