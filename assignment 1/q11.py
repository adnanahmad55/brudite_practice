def sumofdigits(num):
    while num >= 10:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num = num // 10
            print(num)
        num = sum_digits
    return num


num = 987
final_result = sumofdigits(num)

print("Final Output:", final_result)