def solution(s, n):
    answer = ''
    for i in list(s):
      if i == ' ': answer += ' '
      elif 'a' <= i <= 'z':
        if ord('z') < ord(i) + n:
          answer += chr(ord(i) + n - 26)
        else:
          answer += chr(ord(i)+n)
      else:
        if ord('Z') < ord(i) + n:
          answer += chr(ord(i) + n -26)
        else:
          answer += chr(ord(i) + n)
    return answer

