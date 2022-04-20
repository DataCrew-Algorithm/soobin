# 배수와 약수

########################
# 8   16  factor(약수)
# 32  4   multiple(배수)
# 17  5   neither(서로소)
# 0   0
########################

# 방법 1) 
while 4:
    try:
        a, b = map(int, input().split())
        if a < b and b % a == 0:
            print('factor')
        elif a > b and a % b == 0:
            print('multiple')
        elif a != b and a % b != 0 and b % a != 0:
            print('neither')
        elif a == b:
            pass
    except EOFError:
        break

# 방법 2)
while True:
    try:
        a, b = map(int, input().split())
        if a < b and b % a == 0:
            print('factor')
        elif a > b and a % b == 0:
            print('multiple')
        elif a != b and a % b != 0 and b % a != 0:
            print('neither')
        elif a == b:
            pass
    except EOFError:
        break

# 런타임 에러 (EOFError) 발생 시 try ~ except 구문 사용해주면 된다
# 문제에 [입력은 여러 테스트 케이스로 이루어져 있다.]의 기준이 무엇인지 헷갈려
# 예제로 나온 4가지 경우와 무한루프로 도는 경우를 둘 다 구해봤음 (둘다정답)
# while문 무한루프 = while True: