#settings
from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("calculator")
root.geometry("400x200")
root.resizable(width=False,height=False)
color = "gray"
root.configure(bg=color)
#vaty
num1 = StringVar()
num2 = StringVar()
res_value =StringVar()

#frame
top_first = Frame(root,width=400,height=50,bg=color)
top_first.pack(side=TOP)

top_second = Frame(root,width=400,height=50,bg=color)
top_second.pack(side=TOP)

top_third= Frame(root,width=400,height=50,bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root,width=400,height=50,bg=color)
top_forth.pack(side=TOP)
#functions
def errormsg(msg):
    if msg == "error":
        tkinter.messagebox.showerror("Error","somethig went wrong")
    elif msg == "division zero error":
        tkinter.messagebox.showerror("division erro","can not divide by 0")

def plus():
    try:
        valu = float(num1.get()) + float(num2.get())
        res_value.set(valu)
    except:
        errormsg("error for plus function")
    

def minus():
    try:
        valu = float(num1.get()) - float(num2.get())
        res_value.set(valu)
    except:
        errormsg("error for minus function")

def multi():
    try:
        valu = float(num1.get()) * float(num2.get())
        res_value.set(valu)
    except:
        errormsg("error for multipy function")


def divide():
    if num2.get() == "0":
        errormsg("division zero error")
    elif num2.get() != 0:
        try:
            value = float(num1.get()) / float (num2.get())
            res_value.set(value)
        except:
            errormsg("error")

   
 


#buttons
btn_plus = Button(top_third,text="+",width=8,command=lambda:plus())
btn_plus.pack(side=LEFT,padx=5, pady= 5)

btn_minus = Button(top_third,text="-",width=8,command=lambda:minus())
btn_minus.pack(side=LEFT,padx=5, pady= 5)

btn_multi = Button(top_third,text="*",width=8,command=lambda:multi())
btn_multi.pack(side=LEFT,padx=5, pady= 5)

btn_divide = Button(top_third,text="/",width=8,command=lambda:divide())
btn_divide.pack(side=LEFT,padx=5, pady= 5)
#input and label
label_first_number = Label(top_first,text= "input number 1",bg = color)
label_first_number.pack(side=LEFT,pady=5,padx=5)

first_num_input = Entry(top_first,textvariable= num1)
first_num_input.pack(side=LEFT)

label_second_number = Label(top_second,text= "input number 2",bg = color)
label_second_number.pack(side=LEFT,pady=5,padx=5)

second_num_input = Entry(top_second,textvariable= num2)
second_num_input.pack(side=LEFT)


res = Label(top_forth,text= "result",bg = color)
res.pack(side=LEFT,pady=5,padx=5)

res_num = Entry(top_forth,textvariable=res_value)
res_num.pack(side=LEFT)
root.mainloop()



