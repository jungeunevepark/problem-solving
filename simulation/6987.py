import sys
sys.stdin = open("input.txt", "r")

for _ in range(4):
    array = list(map(int, input().split()))
    win, tie, lose = 0, 0, 0
    nonsense = 1
    max_tie, max_lose, max_win = 0, 0, 0
    lose_country, win_country, tie_country = [], [], []

    for i in range(6):
        win += array[3*i]
        tie += array[3*i+1]
        lose += array[3*i+2]
        if not (array[3*i] + array[3*i+1] + array[3*i+2] == 5):
            nonsense = 0
            break
        if array[3*i+1] > 0:
            max_tie = max(array[3*i+1], max_tie)
            tie_country += 1
        if array[3*i] > 0:
            max_lose = max(array[3*i], max_lose)
            win_country += 1
        if array[3*i+2] > 0:
            max_win = max(array[3*i+2], max_win)
            lose_country += 1

    if nonsense == 1:
        if win != lose:
            print(0, end=" ")
        elif tie % 2 != 0:
            print(0, end=" ")
        elif max_tie > tie_country or tie / 2 > tie_country:
            print(0, end=" ")
        elif max_win > win_country:
            print(0, end=" ")
        elif max_lose > lose_country:
            print(0, end=" ")
        else:
            print(1, end=" ")
    else:
        print(0, end=" ")
