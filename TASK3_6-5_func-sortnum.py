# Zaki Zaidan Akbar
# 5007221058
# INTRO TO PROGRAMMING USING PYTHON 6.5 

num1, num2, num3 = map(eval, (input("Enter three numbers (with spaces, not comma):").split()))

def sorted(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort(reverse=True)
    return nums

numbers = sorted(num1, num2, num3)
print("the sorted numbers are ", numbers[0], numbers[1], numbers[2])


