import tkinter as tk

# Initializing my silly stuff that doesn't need silly operations done to add
window = tk.Tk()
window.title("WAWAO")

# initializing operations!
buttons=[]
button_row_0 = tk.Frame()
button_row_1 = tk.Frame(width=100, height=10)
button_row_2 = tk.Frame(width=100, height=10)
button_row_3 = tk.Frame(width=100, height=10)
button_row_4 = tk.Frame(width=100, height=10)
row = [button_row_1, button_row_2, button_row_3, button_row_4]
# UNFUCK THIS
def val(x):
    return x
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def div(x, y):
    return x / y
def mult(x, y):
    return x * y
def enter(num1, num2, operation):
    num3=operation(num1, num2)
    print(num3)
symbolic_operations = ["+","-","/","*","="]
operations = [add, sub, div, mult, enter]

j=0
for i in range (10):
    if (i==0):
        j=3
    btn = tk.Button(
            text=i,
            # unfuck
            command=lambda a=i:val(a),
            master=row[j],
        )
    btn.pack(side=tk.LEFT)
    if ((i)%3==0):
        j=j+1
    if (i==0):
        j=0
    # UNFUCK THIS
    # UNFUCK THIS
    # UNFUCK THIS

btn.pack(side=tk.LEFT)
# creating display for symbols
for i in range (4):
    btn = tk.Button(
        text=symbolic_operations[i],
        command=operations[i],
        master=row[i],
    )
    btn.pack(side=tk.LEFT)
    if (i==3):
        btn = tk.Button(
        text=symbolic_operations[i+1],
        command=operations[i+1],
        master=row[i],
        )
        btn.pack(side=tk.LEFT)
    
    # UNFUCK THIS
    # UNFUCK THIS
    # UNFUCK THIS

button_row_4.pack(side=tk.BOTTOM)
button_row_3.pack(side=tk.BOTTOM)
button_row_2.pack(side=tk.BOTTOM)
button_row_1.pack(side=tk.BOTTOM)


def store (x):
    if x is int:
        ()
# creating display for clear and math display
# store a value comprised of putting in numbers, converting to roman numerals, and then an operation and then start storing a new value 
# might be hard
# append digit 
# display = numStored.toRoman
# display = enter(stored 1, stored 2, stored op).toRoman
# clear = remove stored vars
# creating display for numbers


window.mainloop()
# TO DO:
# basic python learning
# Make buttons again
# execute button_press on tk.Button() click or smth 
# Make working top display
# Convert top display to roman numerals
# figure out what the fuck im doing