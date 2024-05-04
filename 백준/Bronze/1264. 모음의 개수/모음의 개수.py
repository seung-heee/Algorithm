vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
cnt = 0

while True:
    N = input()

    if N == '#':
        break

    for i in N:
        if i in vowel:
            cnt += 1
    print(cnt)
    cnt = 0