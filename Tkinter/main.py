# import tkinter
# # s' obizorom da sve klase pripadaju modulu tkinter
# # mogli smo da ga pozovemo i sa
# # from tkinter import *
# # zvezdica omogucava uvoz svih klasa
# # onda bi nas kod izgledao:
# # window = Tk()
# # my_label = Label()
# # button = Button()
# # ne bi bilo potrebe za pianjem  tkinter. svaki put kada pozivamo klasu iz ovog modula
#
# window = tkinter.Tk()
#
# window.title('                                         Milos voli Sanju')
# window.minsize(width=500, height=300)
#
#
# # Label pokazuje naslov na ekranu, pozicioniran top levo desno dole
#
# my_label =tkinter.Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.pack(side= 'left')#  postavis label na ekran
# # pristupanje elementima klase je kao sa recnikom
# # my_label['text'] = 'Hello, new text!'
# # a moze i sa .config()
# my_label.config(text='Hello, new text!')
#
# # Button
# # prilikom pravljenja buttona, neophodno je da izvrsi i komandu na klik
# # definisemo funkciju koja se izvrsava kada kliknemo na dugme
# def button_clicked():
#     print('i am clicked')
#     challenge = input.get() # challenge da ono sto je u enter upisano izbaci label
#     my_label.config(text= challenge)
#     my_label.pack(side='top')
# # kreiramo dugme i zadajemo mu komandom komandu
# button = tkinter.Button(text= 'click me', command= button_clicked)
# button.pack() # pakujemo ga na ekranu
#
#
# #Entry
# # sluzi za unos podataka
# # kreiramo i postavljamo polje za unos
#
# input = tkinter.Entry(width= 10)
# input.pack()
#
# print(input.get()) # .get() je fja koja skuplja ulaz

from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print(entry.get())
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()





#keep the screen of window always on the in the end
window.mainloop()
