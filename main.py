from tkinter import *

#window
window = Tk()
# window.minsize(400,200)
window.title = "Miles to Km Converter"
window.config(padx=20, pady=40)

#get result

result = "0"

#calculate and display result
def get_result():
    get_num = input.get()
    get_num = float(get_num)
    kilometre = get_num * 1.609
    kilometre = round(kilometre)
    result.config(text=str(kilometre))

#is equal to label

is_equal = Label(text="is equal to", font=("Arial", 20, "bold"))
is_equal.grid(column=0, row=1)
is_equal.config(padx=20, pady=20)

#input box
input = Entry(width=5, font=("Arial", 15))
input.grid(column=1, row=0)

#results label
result = Label(text=result, font=("Arial", 20))
result.grid(column=1, row=1)
result.config(padx=20, pady=20)

#button to calculate
button = Button(text="Calculate", font=("Arial", 15), command=get_result)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

#Miles label
miles = Label(text="Miles",font=("Arial", 15))
miles.grid(column=2, row=0)
miles.config(padx=20,pady=5)

#Km label
km = Label(text="Km",font=("Arial", 12))
km.grid(column=2, row=1)
km.config(padx=20,pady=5)

window.mainloop()