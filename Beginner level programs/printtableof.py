tableof = int(input("enter the number you want the table of :"))

w= int(input("Upto how much counting do you require : "))
w+=1
list= [*range(w)]
i=0
for i in range(w):
    if i==0:
        continue
    answer = tableof*i
    print(tableof, "x",list[i],"=",answer)

print("end of the program ")
