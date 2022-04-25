# 두 수의 합 51696KB / 116ms / 169B

# 9
# [5, 12, 7, 10, 9, 1, 2, 3, 7]
# 13

# 방법1) 시간초과(실패)
# 두 수를 더해 13이 되는 수를 찾기 위한 코드

n = int(input())                             # 첫째줄

sequence = list(map(int,input().split()))    # 둘째줄

X = int(input())                             # 셋째줄

num = []                                     
for i in sequence:
    for j in sequence:
        if i < j and i + j == X:             # 더하는 값의 중복을 피하고자 i < j 조건 넣어줌
            num.append(i)

print(len(num))

# 방법2) 시간 초과(실패)
# 하나하나 다 더하는것이 오래걸린다고 판단하에
# 13에서 수열의 각 요소를 빼어 그 차이가 수열 리스트에 있다면 그 갯수를 세어주는 코드 작성하고자 함
n = int(input())

sequence = list(map(int,input().split()))

X = int(input())

num = []
for i in sequence:
    for j in sequence:
        if X - i == j:           # 뺀 차이가 둘째줄 요소에 있을 경우에만 num 리스트에 넣고자 함
            num.append(i)

print(len(num)/2)

# 방법3) 실패
# 방법2와 내용은 같지만 for문을 한번 사용하고 집합의 교집합을 이용함

n = int(input())

sequence = list(map(int,input().split()))  # [5, 12, 7, 10, 9, 1, 2, 3, 7]
                                             
X = int(input())

num = []
for i in sequence:
    num.append(X - i)                      # [8, 1, 6, 3, 4, 12, 11, 10, 2]

print(len(set(sequence) & set(num))/2)     # 결과값이 3.0으로 나옴 => 혹시 int로 바꾸면?

# 방법4) 방법3의 마지막줄 int 추가
n = int(input())

sequence = list(map(int,input().split()))

X = int(input())

num = []
for i in sequence:
    num.append(X - i) 

print(int(len(set(sequence) & set(num))/2))