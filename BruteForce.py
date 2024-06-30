import itertools
import string
import time


def brute_force(password, charset):
    attempts = 0
    start_time = time.time()
    for length in range(1, 9):  # Limiting to 8 characters for this demo
        for guess in itertools.product(charset, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                end_time = time.time()
                return attempts, end_time - start_time


def main():
    password = input("Enter the password to crack: ")

    charset = string.ascii_lowercase
    charset += string.ascii_uppercase
    charset += string.digits
    charset += string.punctuation

    print("Starting brute force attack...")
    attempts, time_taken = brute_force(password, charset)

    print(f"Password cracked in {attempts} attempts and {time_taken:.2f} seconds")
    print(f"Password: {password}")


if __name__ == "__main__":
    main()
