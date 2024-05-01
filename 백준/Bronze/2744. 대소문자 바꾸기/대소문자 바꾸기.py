word = input()
new = ''
for i in word:
  if i.isupper():
    new += i.lower()
  else:
    new += i.upper()
print(new)