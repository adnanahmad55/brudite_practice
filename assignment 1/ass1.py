x = int(input("Enter a number: "))

if x % 3 == 0 and x % 5 == 0:
    print("BRUDITE - NIRVANA")
elif x % 3 == 0:
    print("SKILLBREW")
elif x % 5 == 0:
    print("BRUDITE")
else:
    print("Not divisible by 3 or 5")