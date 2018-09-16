def FirstNotRepeatingChar(s):
    dict = {}
    for ele in s:
        dict[ele] = 1 if ele not in dict else dict[ele] + 1
    for i in range(len(s)):
        if dict[s[i]] == 1:
            return i
    return -1

print(FirstNotRepeatingChar('abacbcddjrjf'))