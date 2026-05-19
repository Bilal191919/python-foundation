def is_even(n):
    return n % 2 == 0


def factorial(n):
    if n < 0:
        return "Error: negative number"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n <= 0:
        return []
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]


def main():
    print("Even/Odd Checker")
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Error: please enter an integer")
        return
    print("Even" if is_even(n) else "Odd")

    print("\nFactorial Calculator")
    try:
        f = int(input("Enter a number: "))
    except ValueError:
        print("Error: please enter an integer")
        return
    print("Factorial:", factorial(f))

    print("\nFibonacci Series Generator")
    try:
        count = int(input("How many terms? "))
    except ValueError:
        print("Error: please enter an integer")
        return
    print("Series:", fibonacci(count))


if __name__ == "__main__":
    main()
