import random
from datetime import datetime
from unittest import result

from colorama import Fore
import mysql.connector as mysql



db = mysql.connect(host="localhost",
                   user="root",
                   password="12345",
                   database="csproject")
cur = db.cursor()

userid = input(Fore.WHITE + "USERID:")


def user():
    cur.execute("SELECT user, password FROM userinfo;")
    r = cur.fetchall()
    if r:
        for r in cur:
            print('userverified',userid)
        print("WELCOME ", userid)
        db.commit()

    else:
        print("USER NOT FOUND")


def authenticate_user(username, password):
    cur.execute("SELECT user, password FROM userinfo WHERE user=%s AND password=%s", (username, password))
    result = cur.fetchone()
    return result is not None


cur.execute('show databases;')
rows = cur.fetchall()
if ('csproject',) not in rows:
    cur.execute("create database csproject; ")

pwd = input(Fore.GREEN + 'Enter the password:')

if ('csproject',) not in rows:
    cur.execute("create database csproject; ")
    cur.execute("show tables;")
elif ('userinfo',) not in cur:
    cur.execute("insert into userinfo values ('%s','%s');" % (userid, pwd))
    cur.execute('show tables;')
elif ('ende',) not in cur:
    cur.execute(
        "INSERT INTO ENDE (`user`, `password`, `encmsg`, `encpassword`, `encrdmsg`, `date`) on duplicate key update user=values(user)+1;",
        cur.execute('show tables;'))


def profile():
    global userid
    print(userid)


def con():
    ans = input("Do you want to continue(YES(y) or NO(n):")
    if ans == 'y':
        main()
    elif ans == 'n':
        print("PRESENTED BY MARV \n THANK YOU")
    else:
        print("INVALID CHOICE")
        con()


def con1():
    ans = input("Do you want to continue(YES(y) or NO(n):")
    if ans == 'yes':
        confirminguser()
    elif ans == 'no':
        print("PRESENTED BY MARV \n THANK YOU")
    else:
        print("INVALID CHOICE")
        con1()

    # cur.execute("insert table login_page values(id);")


'''def authenticate():
    global pwd
    attempts = 3
    while attempts > 0:
        user_pwd = input(Fore.GREEN + 'Enter the password:')
        if user_pwd == pwd:
            return True
        else:
            attempts -= 1
            print(f'Incorrect password! {attempts} attempts remaining.')
    print('Authentication failed. Exiting...')
    sys.exit()'''


def password():
    cur.execute("SELECT * FROM USERINFO")

    rows=cur.fetchall()
    if rows :
        for K in cur:
            print("YOUR PASSWORD VERIFIED",K)
            db.commit()
            main()

        con()
    else:
        confirminguser()


def password1():
    if pwd == pwd:
        confirminguser()
        return True
    # con1()


def pwdchange():
    global pwd  # Add this line to access the global variable 'pwd'
    oldpwd = input(Fore.GREEN + "Enter the old password: ")
    if oldpwd == pwd:
        newpwd = input(Fore.BLUE + "Enter the new password: ")
        if newpwd != pwd:  # Add this line to check if the new password is different
            pwd = newpwd  # Use the = operator to assign the new password
            print('Password successfully changed.')
            con()
            return True
        else:
            print('New password is the same as the current password. Password not changed.')
            return False
    else:
        print('Old password is incorrect. Password not changed.')
        return False


def profile():
    print(f"User ID: {userid}")
    print(f"Password:{pwd}")


def profile1():
    print("1. Change Password")
    print("2. Return to Main Menu")
    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        pwdchange()

        # print(f"password,pwdchange(new_password)")  # Call the password change function
    elif choice == '2':
        print("Returning to the main menu.")
        con()
    else:
        print("Invalid choice.")


# Define the encrypt function
def encrypt(message, key):
    encrypted_message = ""
    for i in message:
        if i.isalpha():
            shift = ord('a') if i.islower() else ord('A')
            encrypted_char = chr((ord(i) - shift + key) % 26 + shift)
        else:
            encrypted_char = i
        encrypted_message += encrypted_char
    return encrypted_message


# Define the decrypt function
def decrypt(encrypted_message, key):
    return encrypt(encrypted_message, -key)


# Define the password generator function
def passwordgenerator():
    global pwdgen

    lower = input("Enter the lowercase:")
    upper = input("Enter the uppercase:")
    number = int(input("Enter the number:"))
    symbol = input("Enter the symbol you want:")
    length = int(input("Enter the length:"))
    a = 1

    for i in range(a):
        all_chars = lower + upper + symbol + str(number)
        pwdgen = "".join(random.choice(all_chars) for _ in range(length))
        print("The password you have generated is:", pwdgen)
    # db.commit()


#    time.sleep(0.1)


def text_to_braille(text):
    global today
    global n
    global b
    a = {'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
         'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
         'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
         'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
         'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
         'z': '⠵', ' ': ' '}
    result = ''
    for i in text:
        a2 = i.lower()
        if i in a:
            result1 = result + a[a2]
            today = datetime.today().now()
            print(today)
    print(result1)


def braille_to_text(braille):
    a = {'1': "a", '12': "b", '14': "c", '145': "d", '15': "e",
         '124': "f", '1245': "g", '125': "h", '24': "i", '245': "j",
         '13': "k", '123': "l", '134': "m", '1345': "n", '135': "o",
         '1234': "p", '12345': "q", '1235': "r", '234': "s", '2345': "t",
         '136': "u", '1236': "v", '2456': "w", '1346': "x", '13456': "y",
         '1356': "z", ' ': ' '}
    result = ''
    i1 = braille.split()
    for i in i1:
        if i in a:
            result += a[i] + ' '
    print(result)


def encdetails():
    print("Do You Want To See The details :")
    aa1 = input("yes or no:")
    if aa1 == 'yes':
        ab1 = input("Enter the profile password:")
        global pwd
        if ab1 == pwd:
            print("SUCCESSFULLY COLLECTED")
            cur.execute("SELECT * FROM ENDE;")
            rows = cur.fetchall()
            # row: tuple[Union[float, int, Decimal, str, bytes, date, timedelta, datetime, set[str], None], ...]
            for row in rows:
                print(row)
            db.commit()
        else:
            print("Incorrect Password")
            con()


def confirminguser(username, password):
    if authenticate_user(username, password):
        option = input(
            Fore.CYAN + "1.PROFILE \n 2.PASSWORD CHANGE \n 3.ENCRYPTION \n 4.DECRYPTION\n 5.PASSWORD GENERATOR\n "
                        "6.BRAILLE CONVERSION\n 7.DETAILS\nEnter your choice(1-5): ")
        if option.lower() == "1":
            profile()

        elif option.lower() == '2':
            profile1()

        elif option.lower() == "3":
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter the encryption key (an integer): "))
            encrypted_message = encrypt(message, key)
            today = datetime.today()
            today1 = today.isoformat()
            print(today1)
            print("Encrypted message:", encrypted_message)
            cur.execute("INSERT INTO ENDE (`user`, `password`, `encmsg`, `encpassword`, `encrdmsg`, `date`) VALUES "
                        "(%s, %s, %s, %s, %s, %s)on duplicate key update user=values(user)+1;",
                        (userid, pwd, message, key, encrypted_message, today1))
            db.commit()

        elif option.lower() == '4':
            encrypted_message = input("Enter the encrypted message: ")
            key = int(input("Enter the decryption key (an integer): "))
            decrypted_message = decrypt(encrypted_message, key)
            print("Decrypted message:", decrypted_message)

        elif option.lower() == '5':
            passwordgenerator()

        elif option.lower() == '6':
            print("1.TEXT TO BRAILLE\n2.BRAILLE TO TEXT")
            n = int(input("Enter your choice(1-2):"))
            today = datetime.today()
            today2 = today.isoformat()

            if n == 1:
                global result1
                a5 = int(input("Enter how many entries:"))
                for i in range(a5):
                    b = input("Enter your text:")
                    text_to_braille(b)
                    today = datetime.today().now()
                    print(today)
                    cur.execute(
                        "INSERT INTO BRAILLE1(`user`, `password`, `1_0R_2`, `1_TEXT`, `1_BRAILLE`,` NULL`,` NULL`, `date`) VALUES (%s, %s, %s, %s, %s, %s)on duplicate key update user=values(user)+1;",
                        (userid, pwd, n, b, result1 ,today2))


            elif n == 2:
                print("DISCLAIMER: If the given code is wrong; It display a star")
                a5 = int(input("Enter how many entries:"))
                today = datetime.today()
                today3 = today.isoformat()
                for i in range(a5):
                    b1 = input("Enter the code configuration for each letter separated with a space:")
                    braille_to_text(b1)
                    cur.execute(
                        "INSERT INTO BRIALLE2(user, pas"
                        "1sword, 2_TEXT, 2_BRIALLE) VALUES (%s, %s, %s, %s)on duplicate key update user=values(user)+1;",
                        (userid, pwd,b1, result,today3))
            else:
                print("Invalid choice")

        elif option.lower() == '7':
            encdetails()

    else:
        print("INVALIDDDD")


def main():
    try:
        if password() and user():
            print("Login Successful")
            option = input(
                Fore.CYAN + "1.PROFILE \n 2.PASSWORD CHANGE \n 3.ENCRYPTION \n 4.DECRYPTION\n 5.PASSWORD GENERATOR\n "
                            "6.BRAILLE CONVERSION\n 7.DETAILS\nEnter your choice(1-5): ")

            if option.lower() == "1":
                profile()

            elif option.lower() == '2':
                profile1()

            elif option.lower() == "3":
                message = input("Enter the message to encrypt: ")
                key = int(input("Enter the encryption key (an integer): "))
                encrypted_message = encrypt(message, key)
                today = datetime.today()
                today1 = today.isoformat()
                print(today1)
                print("Encrypted message:", encrypted_message)
                cur.execute("INSERT INTO ENDE (`user`, `password`, `encmsg`, `encpassword`, `encrdmsg`, `date`) VALUES "
                            "(%s, %s, %s, %s, %s, %s)on duplicate key update user=values(user)+1;",
                            (userid, pwd, message, key, encrypted_message, today1))
                db.commit()

            elif option.lower() == '4':
                encrypted_message = input("Enter the encrypted message: ")
                key = int(input("Enter the decryption key (an integer): "))
                decrypted_message = decrypt(encrypted_message, key)
                print("Decrypted message:", decrypted_message)

            elif option.lower() == '5':
                passwordgenerator()

            elif option.lower() == '6':
                print("1.TEXT TO BRAILLE\n2.BRAILLE TO TEXT")
                n = int(input("Enter your choice(1-2):"))

                if n == 1:
                    global result1
                    a5 = int(input("Enter how many entries:"))
                    for i in range(a5):
                        b = input("Enter your text:")
                        text_to_braille(b)
                        today = datetime.today().now()
                    print(today)
                    cur.execute(
                        "INSERT INTO BRAILLE(`user`, `password`, `1_0R_2`, `1_TEXT`, `1_BRAILLE`,` NULL`,` NULL`, `date`) VALUES (%s, %s, %s, %s, %s, %s)on duplicate key update user=values(user)+1;",
                        (userid, pwd, n, b, result1, '', '', today))

                elif n == 2:
                    print("DISCLAIMER: If the given code is wrong; It display a star")
                    a5 = int(input("Enter how many entries:"))
                    for i in range(a5):
                        b1 = input("Enter the code configuration for each letter separated with a space:")
                        braille_to_text(b1)

            elif option.lower() == '7':
                encdetails()


        else:
            print("Invalid choice")



    except RecursionError:
        print("INVALIDDDD")

cur.close()
db.close()
main()


