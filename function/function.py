x=int(input("Введите первое число: "))
y=int(input("Введите второе число: "))

def sum(a,b):
    return a + b

def f(a=2):
    return 2*a-2

print(sum(x,y))

print(f(4))
