s = input()
k = int(input())
ans = []
num_parts = len(s) / k
value = len(s) % k

for i in range(int(num_parts)):
    if len(s) % k == 0:
        temp = s[i * k:(i + 1) * k]
    else:
        temp = s[i * k:(i + 1) * k]
    ans.append(temp)

if len(s) % k != 0:
    ans.append(s[int(num_parts) * k:])
print(ans)
for word in ans:
    temp = ''
    for letter in word:
        if letter in temp:
            continue
        else:
            temp += letter
    print(temp)
