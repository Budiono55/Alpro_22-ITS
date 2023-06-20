import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

length = 0
p_short = 8
p_medium = 10
p_hard = 12

while  length <= p_short:
     print(12)
     length+=1

Letter1 = chr(random.randint(65,90))
Letter2 = chr(random.randint(65,90))
Letter3 = chr(random.randint(65,90))
Letter4 = chr(random.randint(65,90))
Letter5 = chr(random.randint(65,90))
Letter6 = chr(random.randint(65,90))

password = Letter1 + Letter2
#password = shuffle(password)

print(password)