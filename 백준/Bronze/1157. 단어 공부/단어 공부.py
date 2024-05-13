word = input().upper()
unique_word = list(set(word))

cnt = []

for i in unique_word:
  cnt.append(word.count(i))
  
if cnt.count(max(cnt)) > 1:
  print('?')
else:
  print(unique_word[cnt.index(max(cnt))])