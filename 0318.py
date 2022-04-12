# number = input()

# type(number) -> str
# list(number) -> str이여서 더해지지 않으므로 int로 바꾸기 위해 map사용
# numbers = list(map(int, list(number)))

# print(sum(int(number),sum(numbers)))
# sum(numbers) = 9
# int(number) = 216
# int(number) + sum(numbers) = 216 + 9 = 

# 망코드 ----------------------------------------

number = int(input()) # 분해합 str로 출력되므로 정수형으로 변환

result = 0 # 생성자를 0이라고 가정하에 시작

for i in range(1, number+1):
    num = list(map(int, str(i)))
    # print(num)
    result = i + sum(num)
    # print(result)

    if result == number:
        print(i)
        break
    elif i == number :
        print(0)




