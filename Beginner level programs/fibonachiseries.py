import array


a = 0
ndlast = 1
last = 1
temp = 0
i=0
fablist = [0]
w=int(input("enter the number of times you want the iterations to occur : "))
for i in range(w):
    a=last + ndlast
    print(a)
    fablist[i] = a

    temp = ndlast
    ndlast = last
    last = fablist[i]

for i in fablist:
    print(i)





