def average_marks(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def main():
    print("Student Marks Average Calculator")
    try:
        count = int(input("How many subjects? "))
    except ValueError:
        print("Error: please enter an integer")
        return

    marks = []
    for i in range(count):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Error: please enter a valid number")

    avg = average_marks(marks)
    print("Average:", round(avg, 2))


if __name__ == "__main__":
    main()
