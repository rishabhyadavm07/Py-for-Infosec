go=[]
print(go)
w=int(input("enter the number of values you want to store in the list: "))
for i in range(0,w):
    c=input("enter the number you want to store: ")
    go.append(c)
print(go)
rin=str(input("do you want to remove any number from the list?(yay/nay)"))
if rin == "yay":
    f=int(input("how many elements to you want to remove :"))
    for i in range(0,f):
        g = str(input("give the value you want to delete: "))
        go.remove(g)
        print(go)
elif rin == "nay":
    print("ending program !")
print("ends")