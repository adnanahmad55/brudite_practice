
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


number1 = 12
number2 = 18
print("LCM of", number1, "and", number2, "is:", lcm(number1, number2))