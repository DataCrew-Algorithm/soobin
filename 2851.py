# 슈퍼 마리오

# 방법 1) - 실패

# mushroom = [int(input()) for _ in range(10)]
# # # 예제 1 input => [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # # 예제 3 input => [40, 40, 40, 40, 40, 40, 40, 40, 40, 40]

# sum1 = mushroom[0] + mushroom[1]      # 30 = 10 + 20
# sum2 = sum1 + mushroom[2]             # 60 = 30 + 30
# sum3 = sum2 + mushroom[3]             # 100 = 60 + 40
# sum4 = sum3 + mushroom[4]             # 150 = 100 + 50
# sum5 = sum4 + mushroom[5]             # 210 = 150 + 60
# sum6 = sum5 + mushroom[6]             # 280 = 210 + 70
# sum7 = sum6 + mushroom[7]             # 360 = 280 + 80
# sum8 = sum7 + mushroom[8]             # 450 = 360 + 90
# sum9 = sum8 + mushroom[9]             # 550 = 450 + 100

# sum_all = [sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9]
# # 예제 1 순차적 합계 => [30, 60, 100, 150, 210, 280, 360, 450, 550]
# # 예제 3 순차적 합계 => [80, 120, 160, 200, 240, 280, 320, 360, 400]

# rest = []              # 합계에서 100을빼고 절대값을 해 줄 리스트 생성
# for i in range(9):
#     rest.append(abs(sum_all[i] - 100))

# # 예제 1 나머지의 절대값 => [70, 40, 0, 50, 110, 180, 260, 350, 450]
# # 예제 3 나머지의 절대값 => [20, 20, 60, 100, 140, 180, 220, 260, 300]

# rest = rest[::-1]

# result = rest.index(min(rest))   

# result = sum_all[result]
# print(result)

# 방법1 피드백(수현님)

mushroom = [int(input()) for _ in range(10)]  # range(9) -> range(10) :피드백

sum1 = mushroom[0]        # sum1 을 mushroom[0]으로 새로 지정
sum2 = sum1 + mushroom[1]            
sum3 = sum2 + mushroom[2]       
sum4 = sum3 + mushroom[3]           
sum5 = sum4 + mushroom[4]          
sum6 = sum5 + mushroom[5]           
sum7 = sum6 + mushroom[6]          
sum8 = sum7 + mushroom[7]          
sum9 = sum8 + mushroom[8]
sum10 = sum9 + mushroom[9]           

sum_all = [sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9, sum10]

rest = []            
for i in range(10): 
    rest.append(abs(sum_all[i] - 100))
# 예제1 print(rest) : [90, 70, 40, 0, 50, 110, 180, 260, 350, 450]
# 예제3 print(rest) : [60, 20, 20, 60, 100, 140, 180, 220, 260, 300]

rest = rest[::-1] 
# 예제1 print(rest) : [450, 350, 260, 180, 110, 50, 0, 40, 70, 90]
# 예제3 print(rest) : [300, 260, 220, 180, 140, 100, 60, 20, 20, 60]

result = rest.index(min(rest))
# 예제1 print(result) : 6
# 예제3 print(result) : 7

sum_all = sum_all[::-1] # 피드백 : sum_all도 거꾸로 배열 후 선택해 줘야함

result = sum_all[result]    

print(result)

# #############################################################################

# # 방법 2) 거꾸로 뽑아서 성공 

# mushroom = [int(input()) for _ in range(10)]

# # 예제 1 input => [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # 예제 3 input => [40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
 


# sum_m = []  # mashroom의 합계를 담을 빈 리스트 생성
# for i in range(10):
#     sum_m.append(sum(mushroom[:10-i]))

# # 예제 1 귀납적 합계 => [550, 450, 360, 280, 210, 150, 100, 60, 30]
# # 예제 3 순차적 합계 => [400, 360, 320, 280, 240, 200, 160, 120, 80]



# rest = []   # 합계에서 100을빼고 절대값을 해준 리스트 생성
# for j in range(10):
#     rest.append(abs(sum_m[j] - 100))

# # 예제 1 나머지의 절대값 => [450, 350, 260, 180, 110, 50, 0, 40, 70]
# # 예제 3 나머지의 절대값 => [300, 260, 220, 180, 140, 100, 60, 20, 20]



# result = rest.index(min(rest))

# # 예제 1 나머지의 절대값이 최소값인 인덱스 : 6
# # 예제 3 나머지의 절대값이 최소값인 인덱스 : 7 (먼저 나온 인덱스를 출력)



# result = sum_m[result]
# print(result)
# # 예제 1 인덱스 6에 해당하는 결과값 : 100
# # 예제 3 인덱스 7에 해당하는 결과값 : 120

# #########################################################################


# mushroom = [int(input()) for _ in range(10)]

# sum_m = [] 
# for i in range(10):
#     sum_m.append(sum(mushroom[:10-i]))

# rest = []   
# for j in range(10):
#     rest.append(abs(sum_m[j] - 100))

# result = rest.index(min(rest))
# result = sum_m[result]
# print(result)