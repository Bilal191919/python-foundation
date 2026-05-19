def star_pattern(rows):
    for i in range(1, rows + 1):
        print("*" * i)


def number_pattern(rows):
    for i in range(1, rows + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        print(line)


def main():
    print("Star Pattern")
    star_pattern(5)

    print("\nNumber Pattern")
    number_pattern(5)


if __name__ == "__main__":
    main()
