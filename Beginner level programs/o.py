tableof=int(input("Enter the number you want table of : "))
till=int(input("Till how much you want the table to be: "))
multiplylist=[]
go=list(range(0,till))
choice=int(input("CHOOSE ONE: \n(1)Output to a file\n (2)Print here! \n : "))
if choice==2:
    for i in range(0,till):
        mulans = tableof * i
        final=tableof, " x ", i, "=",mulans
        print(final)
elif choice==1:
    f=open("Output.txt","a")
    for i in range(0,till):
        mulans = tableof * i
        final = tableof, " x ", i, "=", mulans
        f.write(str(final))
    f.close()


else:
    print("Invalid choice !")







