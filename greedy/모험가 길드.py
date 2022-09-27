from distutils.dir_util import remove_tree


"Fail"
N = int(input())
adventure = list(map(int, input().split()))
adventure.sort()

result = 0    # 총 그룹의 수
count = 0     # 현재 그룹의 모험가 수

for i in adventure:
    count += 1        # 현재 그룹에 해당 모험가를 포함
    if count >= i:    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1   # 총 그룹의 수 증가
        count = 0     # 초기화

"""오름차순으로 정렬된 모험가의 공포도를 확인하며
'현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도'보다
크거나 같다면 그룹으로 설정
항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 됨"""
