A = [False, False] + [True] * 4000000

for i in range(2, 4000000):
    if A[i]:
        for j in range(i+i, 4000000, i):
            A[j] = False
                
a, b, d = map(int, input().split(" "))
sossu = 0
for i in range(a, b+1):
    if A[i]:
        if str(d) in str(i):
            sossu += 1
print(sossu)