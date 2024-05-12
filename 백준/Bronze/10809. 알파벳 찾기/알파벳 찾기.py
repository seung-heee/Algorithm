alphabet = []
S = list(input().lower())
dict = {}


for i in range(97, 123):
  alphabet.append(chr(i))

for i in range(len(S)):
  if S[i] not in dict:
    dict[S[i]] = i

for i in alphabet:
  if (i in dict): print(dict[i], end=' ')
  else: print(-1, end=' ')