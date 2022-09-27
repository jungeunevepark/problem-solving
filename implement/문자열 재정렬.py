input = list(map(ord, input()))
input.sort()

count = 0
for item in input:
    if 48 <= item <= 57:
        count += item - 48
    else:
        print(chr(item), end="")
print(count)
