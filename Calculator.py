import tkinter as tk

# Initializing my silly stuff that doesn't need silly operations done to add
window = tk.Tk()
window.title("Calculator")

# initializing operations!
buttons=[]
button_row_0 = tk.Frame()
button_row_1 = tk.Frame(width=100, height=10)
button_row_2 = tk.Frame(width=100, height=10)
button_row_3 = tk.Frame(width=100, height=10)
button_row_4 = tk.Frame(width=100, height=10)
row = [button_row_1, button_row_2, button_row_3, button_row_4]
symbolic_operations = ["+", "-", "/", "*", "="]
hold=[0]
hold_operation=[]
digit_held=0
# UNFUCK THIS
def val(x):
    storage(x)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    if (y==0):
        y=1
    return x / y

def mult(x, y):
    return x * y


def storage(a):
    global digit_held
    if (isinstance(a, int)):
        hold[digit_held]=hold[digit_held]*10
        hold[digit_held]=hold[digit_held]+a
        print(hold[digit_held])
    else:
        hold_operation.append(a)
        digit_held=digit_held+1
        hold.append(0)
    
    
def enter():
    result=0
    j=0
    for i in range (len(hold)-1):
        result=hold_operation[j](result, hold[i])
        if (j<(len(hold_operation))+1):
            j=j+1
    print(result)

operations = [add, sub, div, mult, enter]

def add_buttons(j):
    for k in range (10):
        if (k==0):
            j=3
        btn = tk.Button(
            text=k,
            # unfuck
            command=storage(k),
            master=row[j],
            )
        btn.pack(side=tk.LEFT)
        if ((k)%3==0):
            j=j+1
        if (k==0):
            j=0
        btn.pack(side=tk.LEFT)

    for k in range (4):
        btn = tk.Button(
            text=symbolic_operations[k],
            command=storage(operations[k]),
            master=row[k],
        )
        btn.pack(side=tk.LEFT)
        if (k==3):
            btn = tk.Button(
            text=symbolic_operations[k+1],
            command=enter,
            master=row[k],
            )
            btn.pack(side=tk.LEFT)

def pack_buttons():
    button_row_4.pack(side=tk.BOTTOM)
    button_row_3.pack(side=tk.BOTTOM)
    button_row_2.pack(side=tk.BOTTOM)
    button_row_1.pack(side=tk.BOTTOM)

def display(value):
    show=tk.frame(
        text=value
    )
    show.Pack(side=tk.TOP)



add_buttons(0)
pack_buttons()

window.mainloop()
