str=input("enter string")
countdigits,countalpha=0,0
for char in str:
    if char.isalpha():
        countalpha+=1
    elif char.isnumeric():
        countdigits+=1    

print(f"the digits in your strings are :{countdigits},and alphabets are :{countalpha}")