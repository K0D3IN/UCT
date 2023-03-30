from cryptography.fernet import Fernet
import os

def clear_screen():
    os.system('clear')

def print_title(title):
    print(f"{'=' * 10} {title} {'=' * 10}\n")

def encrypt_message():
    clear_screen()
    print_title("ENCRYPT A MESSAGE")

    print("1) Encrypt with random key")
    print("2) Encrypt with special key")
    choice = input(">>> ")

    if choice == '1':
        key = Fernet.generate_key()
    elif choice == '2':
        key = input("Enter a key: ").encode()
    else:
        print("Invalid choice!")
        return

    fernet = Fernet(key)
    message = input("Enter your message: ").encode()
    encrypted_message = fernet.encrypt(message)

    print(f"\nYOUR KEY IS = {key.decode()}")
    print("THIS IS YOUR ENCRYPTED MESSAGE:")
    print(encrypted_message.decode())

def decrypt_message():
    clear_screen()
    print_title("DECRYPT A MESSAGE")

    key = input("YOUR SPECIAL KEY>>>").encode()
    message = input("YOUR MESSAGE>>>").encode()

    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(message)

    print(f"\nYOUR DECRYPTED MESSAGE IS: {decrypted_message.decode()}")

def generate_random_key():
    clear_screen()
    print_title("GENERATE RANDOM KEY")

    key = Fernet.generate_key()
    print(key.decode())

def main():
    while True:
        clear_screen()
        print_title("CRYPT")

        print('''CHOOSE OPTION:
        1) ENCRYPT A MESSAGE
        2) DECRYPT A MESSAGE
        3) GENERATE RANDOM KEY
        99) EXIT\n''')

        choice = input(">>> ").encode()

        if choice == b'1':
            encrypt_message()
        elif choice == b'2':
            decrypt_message()
        elif choice == b'3':
            generate_random_key()
        elif choice == b'99':
            exit()
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()
