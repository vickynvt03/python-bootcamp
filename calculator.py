num_1 = int(input("Num 1 : "))
num_2 = int(input("Num 2 : "))
option= int(input("Select 1 for Add, 2 for Sub, 3 for Multiply, 4 for division :"))

def  add(num_1, num_2):
    result = int(num_1 + num_2)
    return result

def  sub(num_1, num_2):
    result = int(num_1 - num_2)
    return result

def  mul(num_1, num_2):
    result = int(num_1 * num_2)
    return result

def  div(num_1, num_2):
    result = int(num_1 / num_2)
    return result

if (option == 1):
    print(add(num_1,num_2))
elif (option == 2):
    print(sub(num_1,num_2))
elif (option == 3):
    print(mul(num_1,num_2))
elif (option == 4):
    print(div(num_1,num_2))
else:
    print(" Not an valid option")
