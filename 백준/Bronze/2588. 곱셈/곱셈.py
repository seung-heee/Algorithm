a = int(input())
b = input()

lst = []
for i in reversed(b):
   lst.append(a * int(i))

print(*lst, sep='\n')
print(a * int(b))