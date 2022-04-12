# 과제 안 내신 분..? (30860KB / 68ms / 160B)
stu = [int(i) for i in range(1,31)]            # 1번 ~ 30번 학생 리스트 생성 

homework = [int(input()) for _ in range(28)]   # 28명의 input값

for j in homework:
    if j in stu:
        stu.remove(j)

print(*stu, sep="\n")
