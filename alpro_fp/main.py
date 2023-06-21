import random
from tkinter import *

length = 0
p_short = 8
p_medium = 12 #med kapital angka
p_hard = 14
p_num = 4

root = Tk()
root.geometry("175x175")

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

value = {
    "Easy":passhort(),
    "Medium":pasmedium(),
    "Hard":pashard()
}

# for(text, value) in value.items():
#     Radiobutton(root, text = text, variable = v,
#                 value = value, indicator = 0,
#                 background="white").pack(fill = X, ipady = 5)

#print(len(user_p))
# password= shuffle(pasmedium())
# print(pasmedium())
# print(password)

print(value["Easy"])

#mainloop()