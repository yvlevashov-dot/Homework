h = list(map(int, input().split()))
n = len(h)

res = [-1] * n
stack = []

for i in range(n):
    while stack and h[stack[-1]] < h[i]:
        stack.pop()
    res[i] = stack[-1] if stack else -1
    stack.append(i)

print(*res)