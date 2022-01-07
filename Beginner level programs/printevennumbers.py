count = int(input("Enter a number till which you want even numbers: "))
if count%2==0:
    count += 2
for i in range(0,count,2):
    print(i)

print("program end")