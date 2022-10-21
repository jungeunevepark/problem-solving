string = input()
l = string.split('-')
answer = 0
for idx, num in enumerate(l):
    new = num
    if '+' in new:
        u = new.split('+')
        new = 0
        for n in u :
            new += int(n)
    if idx == 0:
        answer = int(new)
    else:
        answer -= int(new)
print(answer)