regNo = input()

oddSum, evenSum = 0, 0

for i in range(len(regNo)):
    if int(regNo[i]) % 2 == 0:
        evenSum += int(regNo[i])
    else:
        oddSum += int(regNo[i])

if oddSum == evenSum:
    print("true")
else:
    print("false")
