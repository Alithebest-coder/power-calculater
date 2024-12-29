def add(a,b):
    return a+b
def sub (a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("enter a number for the calculator:   "))
b=int(input("enter a number for the calculator:   "))
print("sum of numbers ", add(a,b))
print("diff of numbers ", sub (a,b))
print("product of numbers ", mul(a,b))
print("quotient of numbers ", div(a,b))