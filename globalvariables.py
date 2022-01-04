print("program start")
x=102
def add():
    print("function called")
    a=4
    b=7
    c=a+b
    global x
    print("sum is ",c)
    print("now printing x :",x)
    x="welcome to this verse"
    print("now the value of x is:",x)
    print("function ends")

add()
print("printing the value of x out of the function",x)#note that the value of the variable x has been changed after we called the function
print("program ends")
