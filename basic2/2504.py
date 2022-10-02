elements = list(input())
stack = []
answer = 0
result = 0

for ele in elements:
    print(answer, result)
    if stack == []:
        answer += result
        result = 0
    if ele == '(' or ele == '[':
        stack.append(ele)
        x = result
        result = 0
    elif ele == ')':
        if stack.pop() == '(':
            if result == 0:
                result = 2
            else:
                result *= 2
        else:
            print(0)
            break
    else:
        if stack.pop() == '[':
            if result == 0:
                result = 3
            else:
                result *= 3
        else:
            print(0)
            break
answer += result
print(answer)
