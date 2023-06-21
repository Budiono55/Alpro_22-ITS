import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

length = 0
p_short = 8
p_medium = 12 #med kapital angka
p_hard = 14
p_num = 4

root = Tk()
root.title('Password Generator')
root.resizable(False, False)
root.geometry("500x300")
root.iconbitmap('alpro_fp\passgen_icon.ico')

label = ttk.Label(
    root, 
    text= 'Password Generator',
    font=("Arial Baltic",12)).pack(ipadx=5, ipady=5)

#Everyday iam Shuffleeeeeing
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#easy version
def passhort():
    user_p = ''
    if len(user_p) <= p_short:
        while len(user_p)<= p_short-p_num:
            user_p += chr(random.randint(ord('a'), ord('z')))
        while len(user_p)<= p_short:
            user_p += str(random.randint(0,9))
    user_p2 = shuffle(user_p)
    return user_p2

#medium version
def pasmedium():
    user_p = ''
    if len(user_p) <= p_medium:
        while len(user_p)<= p_medium-p_num:
            user_p += chr(random.randint(65,90))
        while len(user_p)<= p_medium:
            user_p += str(random.randint(0,9))
    user_p2 = shuffle(user_p)
    return user_p2

#hard version
def pashard():
    user_p = ''
    if len(user_p) <= p_hard:
        while len(user_p)<= p_hard-p_num:
            user_p += chr(random.randint(65,90))
        while len(user_p)<= p_hard:
            user_p += str(random.randint(0,9))
    user_p2 = shuffle(user_p)
    return user_p2

v = StringVar(root, "1")

mode = {
    "Easy":passhort(),
    "Medium":pasmedium(),
    "Hard":pashard()
}

for(text, mode) in mode.items():
    Radiobutton(root, text = text, variable = v,
                value = mode, indicator = 0,
                background="white").pack(fill = X, ipady = 5)

#------------------------------------------------------------------
#Email entry frame
email = tk.StringVar()
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

#Email entry box
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=False)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=False)
email_entry.focus()
#------------------------------------------------------------------

#print(len(user_p))
# password= shuffle(pasmedium())
# print(pasmedium())
# print(password)

# print(mode["Hard"])

label = ttk.Label(
    root, 
    text= 'Password generated:',
    font=("Arial Baltic",10)).pack(ipadx=100, ipady=10)

mainloop()