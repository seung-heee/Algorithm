num = []

for i in range(9):
    num.append(int(input()))

maxNum = max(num)

print(maxNum)
print(num.index(maxNum)+1)