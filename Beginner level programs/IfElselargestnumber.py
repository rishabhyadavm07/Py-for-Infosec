num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))
num4 = int(input("Enter the 4th number: "))

def comparision():
    global num1,num2,num3,num4
    print("function called !")
    if num1 > num2 and num1 > num3 and num1 > num4:
        print(num1, "is the greatest !")
    if num2 > num1 and num2 > num3 and num2 > num4:
        print(num2, "is the greatest !")
    if num3 > num2 and num3 > num1 and num3 > num4:
        print(num3, "is the greatest !")
    if num4 > num2 and num4 > num3 and num4 > num1:
        print(num4, "is the greatest !")
    print("function ends")


print("calling function1")
comparision()
print("end of the program")


