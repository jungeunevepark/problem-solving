import sys
sys.stdin = open("input.txt", "r")
one = list(input())
two = list(input())
array = ""
for i in range(len(one)):
    array += one[i]
    array += two[i]

while len(array) > 2:
    answer = ""
    for i in range(len(array)-1):
        answer += str((int(array[i]) + int(array[i+1])) % 10)
    array = answer
print(array)
