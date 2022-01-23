from tkinter import *


window = Tk()
window.title('Miles to Km Converter')# if we want to resize a window use command: window.minsize(width=250, height=250)
window.config(padx=20,pady=20)

enter = Entry(width=10)# if we want to enter a text we use command: enter.insert(END, string="insert miles")
enter.grid(row=0,column=1)

is_equal_label= Label(text='is equal to')
is_equal_label.grid(row=1, column=0)

miles_label=Label(text='Miles')
miles_label.grid(row=0, column=2)

km_label=Label(text='Km')
km_label.grid(row=1, column=2)

answer_label = Label(text='0')
answer_label.grid(row=1,column=1)

def calculate_when_button_click():
    km = float(enter.get())
    km = round(km*1.609, 4)
    answer_label.config(text=km)
    
button = Button(text='calculate',command=calculate_when_button_click)
button.grid(row=2,column=1)


window.mainloop()