x=int(input("enter the starting number"))
y=int(input("enter the ending number"))
sum=0
for i in range(x,y):
    if(i%2!=0):
        sum+=i
print(sum)        