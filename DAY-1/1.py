nums = list(map(int, input().split(", ")))
ans = []
for num in nums:
    if nums.count(num) == 1:
        ans.append(num)

print(ans)