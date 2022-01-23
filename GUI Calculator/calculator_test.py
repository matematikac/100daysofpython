from tkinter import *


AQUA =	'#00FFFF'
window = Tk()
window.title('CALCULATOR')
window.minsize(width=200,height=200)
window.config(padx=30,pady=40,bg=AQUA)

def new_calculation():
    new_calculation_button.destroy()

    first_text = Label(text="First number:",font=('Ariel',15),fg='blue')
    first_text.grid(row=0, column=0)

    first_num_entry = Entry(width=10)
    first_num_entry.grid(row=0, column=2)

    operation_text = Label(text="Choose operation:", font=('Ariel', 15), fg='blue')
    operation_text.grid(row=1, column=1)

    # Listbox of operation
    def listbox_used(event):
        pass

    listbox = Listbox(height=4, width=3)
    operation =['+' , '-' , '*', '/'] #["+ Add", "- Subtract", "* Multiply", "/ Divide"]
    for item in operation:
        listbox.insert(operation.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.grid(row=1, column=2)

    second_text = Label(text="Second number:",font=('Ariel',15),fg='blue')
    second_text.grid(row=2, column=0)

    second_num_entry = Entry(width=10,highlightthickness=0)
    second_num_entry.grid(row=2, column=2)

    def result():
        first = first_num_entry.get()
        second = second_num_entry.get()
        operation_choise = listbox.get(listbox.curselection())
        try:
            first = float(first)
            second = float(second)

            if operation_choise =='/' :
                if second==0:
                    result = 'not defined'
                else:
                    result = round(first / second, 4)
            elif operation_choise == '-':
                result = round(first - second, 4)
            elif operation_choise == '+' :
                result = round(first + second, 4)
            else:
                result = round(first*second, 4)

            result_text = Label(text='{}{}{}={}'.format(first, operation_choise, second, result),font=('Ariel',15),fg='blue',bg='yellow')
            result_text.grid(row=4, column=1)
        except ValueError:
            first_text.destroy()
            first_num_entry.destroy()
            second_text.destroy()
            second_num_entry.destroy()
            operation_text.destroy()
            listbox.destroy()
            result_button.destroy()
            result_text = Label(text="Please, insert float number.",font=('Ariel',15,'bold'),fg='red')
            result_text.grid(row=4, column=1)

        first_text.destroy()
        first_num_entry.destroy()
        second_text.destroy()
        second_num_entry.destroy()
        operation_text.destroy()
        listbox.destroy()
        result_button.destroy()

        def clear():
            result_text.destroy()
            clear_button.destroy()
            new_calculation()

        clear_button = Button(text="clear", command=clear,highlightthickness=0,font=('Ariel',15),fg='red')
        clear_button.grid(row=5, column=1)

    result_button = Button(text="result=", command=result,highlightthickness=0,font=('Ariel',15,'bold'),fg='green')
    result_button.grid(row=3, column=2)

new_calculation_button = Button(text="new_calculation", font=('Ariel',15),command=new_calculation,highlightthickness=0,bg='yellow',fg='red')
new_calculation_button.grid(row=0, column=0)
window.mainloop()