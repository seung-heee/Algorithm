def solution(s, pat):
    for idx, value in enumerate(s):
        if value == "A":
            s = s[:idx] + "B" + s[idx + 1 :]
        else:
            s = s[:idx] + "A" + s[idx + 1 :]

    return int(pat in s)
