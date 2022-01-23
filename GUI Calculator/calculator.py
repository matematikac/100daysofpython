from tkinter import *

window = Tk()
window.title('CALCULATOR')
window.minsize(width=600,height=600)
window.config(padx=30,pady=40)
# First number
# first number button
def new_calculation():
    def action():
        try:
            first = float(first_num.get())
            # Listbox of operation
            def listbox_used(event):
                operation = listbox.get(listbox.curselection())
                # Second number
                # second number button
                def action2():
                    listbox.destroy()
                    try:
                        second = float(second_num.get())
                        result = first + second
                        label = Label(text="Result is: {}".format(result))
                        label.grid(row=3, column=1)
                        print("Do something")
                    except ValueError:
                        label = Label(text="Please, insert float number.")
                        label.grid(row=1, column=0)

                # calls action2() when pressed
                button2 = Button(text="Second number:", command=action2)
                button2.grid(row=2, column=0)
                # second number entry
                second_num = Entry(width=10)
                second_num.grid(row=2, column=1)
            listbox = Listbox(height=4)
            operation = ["+ Add", "- Subtract", "* Multiply", "/ Divide"]
            for item in operation:
                listbox.insert(operation.index(item), item)
            listbox.bind("<<ListboxSelect>>", listbox_used)
            listbox.grid(row=1, column=1)

        except ValueError:
            label = Label(text="Please, insert float number.")
            label.grid(row=1, column=0)
        print("Do something")

    #calls action() when pressed
    button = Button(text="First number:", command=action)
    button.grid(row=0, column=0)
    # first number entry
    first_num = Entry(width=10)
    first_num.grid(row=0, column=1)
#calls new_calculation() when pressed
button = Button(text="new_calculation", command=new_calculation)
button.grid(row=4, column=1)


window.mainloop()