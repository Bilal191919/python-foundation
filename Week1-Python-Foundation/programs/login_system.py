def check_login(username, password):
    return username == "admin" and password == "1234"


def main():
    print("Simple Login System")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if check_login(username, password):
        print("Login successful")
    else:
        print("Invalid credentials")


if __name__ == "__main__":
    main()
