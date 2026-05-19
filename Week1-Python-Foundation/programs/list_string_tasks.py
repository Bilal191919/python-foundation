def largest_number(numbers):
    if not numbers:
        return None
    return max(numbers)


def reverse_string(text):
    return text[::-1]


def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)


def remove_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def main():
    numbers = [3, 8, 1, 9, 2]
    print("Largest number:", largest_number(numbers))

    text = "Hello Interns"
    print("Reversed string:", reverse_string(text))

    sentence = "Python makes problem solving easy"
    print("Vowel count:", count_vowels(sentence))

    items = [1, 2, 2, 3, 1, 4, 4]
    print("Without duplicates:", remove_duplicates(items))


if __name__ == "__main__":
    main()
