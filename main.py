import random
import string
import subprocess

# init variables and set letters and symbols using the string library
password = ""
letters = string.ascii_letters
symbols = string.punctuation

# take input for user to select password length and cast to integer
while True:
    try:
        num_chars = int(input("Select the number of characters for your password: "))

        # decrement until 0 and return a password of random ascii chars of the desired length
        while num_chars >= 0:
            random_char = letters + symbols
            password += random_char[random.randint(0, (len(random_char) - 1))]
            num_chars -= 1

        # print generated password
        print(f"Your generated password is: {password} and it is copied to your clipboard.")

        # copy generated password to clipboard
        subprocess.call(f"echo \"{password}\" | pbcopy")

        break

    # catch erroneous input
    except ValueError:
        print("Needs to be an integer (1, 2, 3 etc..). Longer is better")
