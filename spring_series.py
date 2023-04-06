K1 = eval(input("K1 constant "))
K2 = eval(input("K2 constant "))
K3 = eval(input("K3 constant "))

F = eval(input("Force desired: "))

spring_series= 1/((1/K1)+(1/K2)+(1/K3))

elongation = F/spring_series

print("The elongation happened in ur case is", elongation)