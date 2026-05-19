def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    return "Error: invalid operator"


def main():
    print("Simple Calculator")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
    except ValueError:
        print("Error: please enter valid numbers")
        return

    result = calculate(a, b, op)
    print("Result:", result)


if __name__ == "__main__":
    main()
