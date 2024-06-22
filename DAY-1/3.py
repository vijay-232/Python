s = input()
k = int(input())
ans = []
if len(s) % k == 0:
    for i in range(k):
        ans.append(s[i * k:(i + 1) * k])
elif len(s) % k != 0:
    for i in range(len(s) % k):
        ans.append(s[i * k:(i + 1) * k])
    ans.append(s[(len(s) % k) * k:])

for word in ans:
    temp = ''
    for letter in word:
        if letter in temp:
            continue
        else:
            temp += letter
    print(temp)
