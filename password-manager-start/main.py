from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(letter) for letter in letters[:nr_letters]]
    [password_list.append(symbol) for symbol in symbols[:nr_symbols]]
    [password_list.append(number) for number in numbers[:nr_numbers]]
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)
    messagebox.showinfo('Title', 'Password has been copied to clipboard')



# ---------------------------- SAVE PASSWORD ------------------------------- #

## Create a function that takes the website, email and password and stores it in a local txt file with formatting.
# Make open and write to TXT file
# Create a function
# Format the output
def password_storer():
    password_text = password_entry.get()
    email_username_text = email_username_entry.get()
    website_text = website_entry.get()

    # TODO Add popups to stop the user when the password or user is empty
    if len(email_username_text) < 1:
        messagebox.showinfo('Alert', 'The email or username is too short')
    elif len(password_text) < 1:
        messagebox.showinfo('Alert', 'The password is too short')
    elif len(website_text) < 1:
        messagebox.showinfo('Alert', 'The website is too short')
    else:
        website_entry.delete(0, END)
        email_username_entry.delete(0, END)
        password_entry.delete(0, END)

        is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nEmail: {email_username_text}\n Password:{password_text}\nIs it okay to save?")

        if is_ok:
            with open('saved_passwords.txt', 'a') as f:
                formatted_data = f"{website_text} | {email_username_text} | {password_text}\n"
                f.write(formatted_data)
        else:
            print('The user chose not to save!')

# Clean the entries when add is pressed. .delete().


# ---------------------------- UI SETUP ------------------------------- #

## Starting tkinter and initializing a new window.
window = Tk()
window.title('Password Manager')
window.minsize(width='200', height='200')
window.config(padx=20,pady=20)


## MyPass Logo
## We can use Canvas to create/import images into Tkinter.
canvas = Canvas(width=200, height=200)
## The image must be stated as a variable using the PhotoImage() method.
main_logo = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=main_logo)
canvas.grid(column=1,row =0)

## Labels
# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0,row =1)
# Email/Username Label
email_label = Label(text="Email:")
email_label.grid(column=0,row =2)
# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0,row =3)

## Entries
# Website Entry
website_entry = Entry(width=38)
website_entry.grid(column=1,row =1, columnspan=2)
website_entry.focus()
# Email/Username Entry
email_username_entry = Entry(width=38)
email_username_entry.grid(column=1,row =2, columnspan=2)
email_username_entry.insert(0,'this_is_a_test@test.com')
# Password Entry
password_entry = Entry(width=21)
password_entry.grid(column=1,row =3)

## Buttons
# Generate Password Button
def action_1():
    print("Do something")
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2,row=3)
# Add Button
def action_2():
    print("Do something")
add_button = Button(text="Add", command=password_storer, width=36)
add_button.grid(column=1,row =4, columnspan=2)



window.mainloop()


