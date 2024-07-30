import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
