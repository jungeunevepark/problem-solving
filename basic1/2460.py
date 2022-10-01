total = 0
result = 0
for _ in range(10):
    outp, inp = map(int, input().split())
    total = total - outp + inp
    if inp > outp:
        result = max(result, total)
print(result)
