from tkinter import *
# playing with pack place grid and padding
#Creating a new window and configurations
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#padding(padx=... , pady=...) daje prostora iliti odbija od ivica prozora
window.config(padx=100, pady=50)


#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
#label.pack() umesto .pack() mozemo da pozicioniramo sa place(x=...,y=...)

#label.place(x=0, y=0)
# a mozemo i sa grid, koji pravi matricu row x columns
# NE MOZE GRID I PACK U ISTOM KODU!
label.grid(row=0,column=0)
label.config(padx=50, pady=50)
#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Button", command=action)
button.grid(row=1,column=1)

#new Button
def action():
    print("Do something")

#calls action() when pressed
new_button = Button(text="New Button", command=action)
new_button.grid(row=0,column=2)

#Entries
input = Entry(width=10)
input.grid(row=2,column=3)
input.get()


#keep the screen of window always on the in the end
window.mainloop()
