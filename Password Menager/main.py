from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    if len(password_entry.get())== 0:
        password_entry.insert(0, ''.join(password_list))
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, ''.join(password_list))
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    w = website_entry.get()
    u = username_entry.get()
    p = password_entry.get()

    if len(w)==0:
        messagebox.showwarning(title='WARNING',message='enter website name')
    elif len(u)==0:
        messagebox.showwarning(title='WARNING', message='enter email/username')
    elif len(p) == 0:
        messagebox.showwarning(title='WARNING', message='chose password ')
    else:
        is_ok = messagebox.askokcancel(title= u, message='Do you want to save\npassword: {}\nfor website: {}\n'.format(p,w))
        if is_ok :
            with open('data.txt', 'a') as f:
                f.write('website_name: {} / email_or_username: {} / password: {} \n'
                        '-------------------------------------------------------------------------------------------------------\n'.format(w, u, p))
                messagebox.showinfo(title='Info',message='Your password is added to data.txt')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.configure(padx=50,pady=50,bg='#84cbdf')


canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

#Labels
website = Label(text='Website:')
website.grid(row=1,column=0)

username = Label(text='Email/Username:')
username.grid(row=2,column=0)

password = Label(text='Password:')
password.grid(row=3,column=0)

# Entry
website_entry = Entry(width=45)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()# positioning the cursor in this entry

username_entry = Entry(width=45)
username_entry.grid(row=2,column=1,columnspan=2)
username_entry.insert(0,'milos_d_markovic@yahoo.com')

password_entry = Entry(width=25)
password_entry.grid(row=3,column=1)

generate_password_button= Button(text='Generate Password',width=15,command=generate_password)
generate_password_button.grid(row=3,column=2)


add_button= Button(text='Add',width=46,command=add)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()