# 소트인사이드 30840KB / 72m / 103B

N = input()

num = []

for i in N:
    num.append(i)
    num.sort()
    num.reverse()

print(*num, sep='')