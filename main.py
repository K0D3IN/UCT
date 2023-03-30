from cryptography.fernet import Fernet
import os


def main():
    os.system("clear")
    os.system("figlet CRYPT")
    print('''CHOOSE OPTION:
    1)ENCRYPT A MESSAGE
    2)DECRYPT A MESSAGE
    3)GENERATE RANDOM KEY
    99)EXIT
    ''')
    opt = int(input(">>>"))
    if opt == 1:
        sifre()
    elif opt == 2:
        coz()
    elif opt == 3:
        random()
    elif opt == 99:
        exit()


def sifre():
    os.system("clear")
    os.system("figlet CRYPT")
    print("1)Encrypt with random key\n2)Encrypt with special key")
    c = int(input(">>>"))
    if c == 1:
        os.system("clear")
        key = Fernet.generate_key()
        fernet = Fernet(key)
        message = input("YOUR MESSAGE>>>")
        b = bytes(message, 'utf-8')
        e_message = fernet.encrypt(b)
        print("YOUR KEY IS =", key)
        print("YOUR KEY IS WILL LOOK LIKE THIS b'xxx' DELETE THE 'b' AND QUOTATION MARKS")
        print("THIS IS YOUR ENCRYPTED MESSAGE", e_message)
    if c == 2:
        os.system("clear")
        key = input("YOUR KEY")
        fernet = Fernet(key)
        message = input("YOUR MESSAGE>>>")
        e_message = fernet.encrypt(message)
        print("THIS IS YOUR ENCRYPTED MESSAGE", e_message)


def coz():
    os.system("clear")
    key = input("YOUR SPECIAL KEY>>>")
    message = input("YOUR MESSAGE>>>")
    fernet = Fernet(key)
    d_message = fernet.decrypt(message)
    print(d_message)


def random():
    key = Fernet.generate_key()
    print("YOUR KEY IS WILL LOOK LIKE THIS b'xxx' DELETE THE 'b' AND QUOTATION MARKS")
    print(key)


main()
