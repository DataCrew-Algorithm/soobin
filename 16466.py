# 콘서트 207092KB / 600ms / 304B

n = int(input())
first_ticket = list(map(int,input().split()))             # [4, 1, 2, 7, 8]

number = []
for i in range(1,n+1):
    number.append(i)                                      # [1, 2, 3, 4, 5]

second_ticket = list(set(number) - set(first_ticket))     # [3, 5]

if second_ticket != [] and second_ticket[0] in number:    # 3
    print(min(list(second_ticket)))
elif second_ticket == []:
    print(n+1)
