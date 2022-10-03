import sys
sys.stdin = open("input.txt", "r")
value = list(input().split())

for ele in value:
    if ele == value[0]:
        continue
    print(value[0], end="")
    result = ""
    val = " "
    for s in ele:
        if s == ',' or s == ';' or s == ']':
            continue
        if s == '[':
            result = "[]"+result
        elif s == '*' or s == '&':
            result = s+result
        else:
            val += s
    result += val + ";"
    print(result)
