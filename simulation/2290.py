s, n = input().split()
array = list(n)
s = int(s)

up = ""
mid1 = ""
mid = ""
mid2 = ""
down = ""

for i in array:
    if i in ['2', '3', '5', '6', '7', '8', '9', '0']:
        up += ' '+'-'*s + '  '
    else:
        up += ' '*(s+3)
    if i in ['4', '5', '6', '8', '9', '0']:
        mid1 += "|" + " "*s
    else:
        mid1 += ' '*(s+1)
    if i in ['1', '2', '3', '4', '7', '8', '9', '0']:
        mid1 += "| "
    else:
        mid1 += '  '
    if i in ['2', '3', '4', '5', '6', '8', '9']:
        mid += ' '+'-'*s + '  '
    else:
        mid += ' '*(s+3)
    if i in ['2', '6', '8', '0']:
        mid2 += "|" + " "*s
    else:
        mid2 += " "*(s+1)
    if i in ['1', '3', '4', '5', '6', '7', '8', '9', '0']:
        mid2 += '| '
    else:
        mid2 += '  '
    if i in ['2', '3', '5', '6', '8', '9', '0']:
        down += ' '+'-'*s + '  '
    else:
        down += ' '*(s+3)

print(up)
for _ in range(s):
    print(mid1)
print(mid)
for _ in range(s):
    print(mid2)
print(down)
