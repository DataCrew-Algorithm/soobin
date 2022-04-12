# 수 정렬하기

# 방법 1)
num = int(input())               # 첫번째 줄 숫자 써주는 input 
 
result = []                      # 결과 담아줄 빈 리스트  

for _ in range(num):             # 두번째줄부터 숫자 써주는 input 길이(num에 따라 달라진다)
    result.append(int(input()))  # 입력받은 숫자 result에 넣어줌

result.sort()                    # 오름차순 정렬

for i in result:                 # 하나씩 결과값 출력
    print(i)

###############################################################################################
# 방법 2)
num = int(input())               # 첫번째 줄 숫자 써주는 input 
 
result = []                      # 결과 담아줄 빈 리스트  

for _ in range(num):             # 두번째줄부터 숫자 써주는 input 길이(num에 따라 달라진다)
    result.append(int(input()))  # 입력받은 숫자 result에 넣어줌

result.sort()                    # 오름차순 정렬

result = str(result)             # replace 함수 사용하기 위해 문자열로 바꿔줌 (replace함수는 list형태에서 사용 불가)
result = result.replace('[','').replace(',','\n').replace(' ','').replace(']','') 
                                 # [1, 2, 3, 4, 5]에서 대괄호 없애기 / 쉼표는 줄바꿈 / 공백 없애기
print(result)

