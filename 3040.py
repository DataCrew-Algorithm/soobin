# 백설공주와 난쟁이 (30864KB, 72ms)

dwarfs = [int(input()) for _ in range(9)]         # [7, 8, 10, 13, 15, 19, 20, 23, 25] <class 'list'>

sum_dwarfs = sum(dwarfs)                            # 아홉 난쟁이의 모자의 숫자 합계

rest = sum_dwarfs - 100                             # 나머지 = 아홉 난쟁이의 모자의 숫자 합계 - 100

for i in dwarfs:
    for j in dwarfs:
        if i + j == rest and i != j and i < j:  # 두개를 골라 합이 rest와 같은 i와 j를 찾는다(단, i와 j는 같지않으며 i는 j보다 작다고 설정 (그래야 중복해서 결과가 나오지 않음))
            num1 = i
            num2 = j

dwarfs.remove(num1)  # dwarfs에서 num1, num2 제거
dwarfs.remove(num2)

for real_dwarfs in dwarfs:
    print(real_dwarfs)
