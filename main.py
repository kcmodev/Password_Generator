import random
import string
import os
import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Password Generator")
window.geometry("355x245+600+300")

for i in range(5):
    window.rowconfigure(i, weight=1)
    window.columnconfigure(i, weight=1)

# init variables and set letters and symbols using the string library
password = ""
num_chars = []
letters = string.ascii_letters
symbols = string.punctuation

# exclude symbols that will cause issues with the terminal command or
# are commonly not acceptable password characters
unwanted_symbols = ['\"', '|', '`', '(', ')', '[', ']', '^', '.']

for symbol in unwanted_symbols:
    symbols = symbols.replace(symbol, '')


def generate():
    global password, letters, symbols
    # take input for user to select password length and cast to integer
    while True:
        try:
            # num_chars = int(
            #     input("Select the number of characters for your password: "))

            # decrement until 0
            # return a password of random ascii chars of the desired length
            # while num_chars >= 0:
            #     random_char = letters + symbols
            #
            #     password += random_char[random.randint(0, (len(random_char) - 1))]
            #     num_chars -= 1

            # print generated password
            print(f"Your generated password is: {password} "
                  f"and it is copied to your clipboard.")

            # copy generated password to clipboards
            os.system(f"echo -E \"{password}\" | pbcopy")

            break

        # catch erroneous input
        except ValueError:
            print("Needs to be an integer (1, 2, 3 etc..). Longer is better")


select_text = ttk.Label(window, text="Number of chars?", background="blue")
select_text.grid(row=0, column=0)

for num in range(0, 10):
    num_chars.append(num)

num_of_chars = ttk.Combobox(window, justify="center", values=num_chars)
num_of_chars.grid(row=0, column=2, width=10)

password_field = ttk.Entry(window, justify="center", textvariable=password,
                           font="Calibri 18")
password_field.grid(row=3, column=2)

generate_button = ttk.Button(window,
                             text="Generate", command=lambda: generate())
generate_button.grid(row=4, column=2)
window.mainloop()
