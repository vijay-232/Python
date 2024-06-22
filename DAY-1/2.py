s = input().split()
ans = {}

for word in s:
    ans[word] = s.count(word)

print(ans)