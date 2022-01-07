str = "akash is good"
# print(str[:7])
for i in str:
    if i=="a":
        continue
    if i=="g":
        break
    print(i)
print("program end")