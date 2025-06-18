inputlist = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency = {}
for item in inputlist:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1


print("Frequency count:", frequency)