digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(digits)):
    print(digits[0:i])
    print(digits[0:-i])

print('************************************************************\n')

for i in range(len(digits)-2):
    print(digits[i:i+3])
