n = int(input()) # 모험가 수
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1 # 현재 그룹에 해당 모험가 포함시키기
    if count >= i: # 만약 모험가수가 공포도 이상이라면, 그룹 결성
        result += 1
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
        
print(result) # 총 그룹수