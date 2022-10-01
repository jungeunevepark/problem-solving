import sys
sys.stdin = open("input.txt", "r")


def quick_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array
    pivot = array[0]
    tail = array[1:]
    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


for _ in range(int(input())):
    array = quick_sort(list(map(int, input().split())))
    print(array[7])
