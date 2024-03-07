def check_username_length(username, min_length):
    return len(username) >= min_length


def main():
    username = input('Enter your username: ')
    min_length = 6
    if check_username_length(username, min_length):
        print(f"Username '{username}' has at least {min_length} characters")
    else:
        print(f"Username '{username}' does not have at least {min_length} characters")


if __name__ == "__main__":
    main()