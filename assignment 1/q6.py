
def is_perfect(num):
    if num <= 0:
        return False
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num


n = int(input("Enter a number: "))


if is_perfect(n):
    print("Yes")
else:
    print("No")