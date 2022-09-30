
def add(x,z):
    if type(x) or type(z) is not int:
        raise ValueError("numbers must be an integer")
    return x + z

def substract(x,z):
    if type(x) or type(z) is not int:
        raise ValueError("numbers must be an integer")
    return x - z

def multiplay(x,z):
    if type(x) or type(z) is not int:
        raise ValueError("numbers must be an integer")
    return x * z

def divide(x,z):
    if x <0 or z <0:
        raise ValueError ("parametrs must be positive")
    if type(x) or type(z) is not int:
        raise ValueError("numbers must be an integer")
    if x == 0 or z ==0:
         raise ValueError ("numbers cant be divide by zero (0)")
    return x / z

print(" my mini calculator! select an operation ")
print("a - add")
print("b - substract")
print("c - multiplay")
print("d - divide")

choice = input(" please enter your choice (a/b/c/d) : ")

num_1 = int (input(" please enter the first number :"))
num_2 = int (input(" please enter the second number :"))

if choice == 'a':
    print (num_1 ,  " + " , num_2, " = ", add(num_1,num_2))

elif choice == 'b':
    print (num_1 ,  " - " , num_2, " = ", substract(num_1,num_2))

elif choice == 'c':
    print (num_1 ,  " * " , num_2, " = ", multiplay(num_1,num_2))

elif choice == 'd':
    print (num_1 ,  " / " , num_2, " = ", divide(num_1,num_2))

else:
    print(" invalid choice/input ):")


