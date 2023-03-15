#bmi
weight = eval(input("enter weight in kilogram"))

height = eval(input("enter height in meter"))

bmi = weight / (height*height)

if bmi <10.5 :
    print ("underweight u skinny ahh")
elif bmi < 25 :
    print ("aint no way its just right u gotta be at least under/overweight bro no cap ngl ur braindead ash lool")
elif bmi < 35 :
    print ("overweight af looool")
else:
    print ("ur not human istg")