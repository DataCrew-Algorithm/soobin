# 탄산음료 (피드백 확인하기)

# 현재 가지고 있는 빈병 | 길에서 발견한 빈병 | 새병 바꾸는데 필요한 빈병
#          e                    f                      c
#          9                    0                      3
#           (0 0 0) (0 0 0) (0 0 0)
#             (★      ★     ★)    -> new1 : 3
#                      ★            -> new2 : 1
#                                    -> new1 + new2 = 4

# 현재 가지고 있는 빈병 | 길에서 발견한 빈병 | 새병 바꾸는데 필요한 빈병
#          e                    f                      c
#          5                    5                      2
#           (0 0) (0 0) (0 0) (0 0) (0 0)
#            (★   ★)   (★    ★)       -> new1 : 5
#               (★         ★)       |    -> new2 : 2
#                     (★            ★)   -> new3 : 1
#                              ★          -> new4 : 1
#                                          -> new1 + new2 + new3 + new4 = 9
#    

# 반복 실행 횟수가 명확하지않을때 while문 ... 근데 어떻게 ?

e, f, c = map(int, input().split())

empty_bottle = e + f

new_bottle = empty_bottle // c
new_bottle = new_bottle // c
print(new_bottle)


new_bottle = 0

while new_bottle < empty_bottle:
    new_bottle = empty_bottle // c
print(new_bottle)


