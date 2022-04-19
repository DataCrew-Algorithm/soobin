# 저항 30840KB / 72ms / 1417B

# black    0    1   = 10^0
# brown    1    10  = 10^1
# red      2    100 = 10^2

# case1) 비효율적 (코드 김)

color = []

for _ in range(3):
    color.append(input())

# value_1 찾기
if color[0] == 'black':
    value_1 = '0'
elif color[0] == 'brown':
    value_1 = '1'
elif color[0] == 'red':
    value_1 = '2'
elif color[0] == 'orange':
    value_1 = '3'
elif color[0] == 'yellow':
    value_1 = '4'
elif color[0] == 'green':
    value_1 = '5'
elif color[0] == 'blue':
    value_1 = '6'
elif color[0] == 'violet':
    value_1 = '7'
elif color[0] == 'grey':
    value_1 = '8'
elif color[0] == 'white':
    value_1 = '9'

# value_2 찾기
if color[1] == 'black':
    value_2 = '0'
elif color[1] == 'brown':
    value_2 = '1'
elif color[1] == 'red':
    value_2 = '2'
elif color[1] == 'orange':
    value_2 = '3'
elif color[1] == 'yellow':
    value_2 = '4'
elif color[1] == 'green':
    value_2 = '5'
elif color[1] == 'blue':
    value_2 = '6'
elif color[1] == 'violet':
    value_2 = '7'
elif color[1] == 'grey':
    value_2 = '8'
elif color[1] == 'white':
    value_2 = '9'

# 곱 찾기
if color[2] == 'black':
    times = 1
elif color[2] == 'brown':
    times = 10
elif color[2] == 'red':
    times = 100
elif color[2] == 'orange':
    times = 1000
elif color[2] == 'yellow':
    times = 10000
elif color[2] == 'green':
    times = 100000
elif color[2] == 'blue':
    times = 1000000
elif color[2] == 'violet':
    times = 10000000
elif color[2] == 'grey':
    times = 100000000
elif color[2] == 'white':
    times = 1000000000

v = value_1 + value_2

print(int(v)*times)

# ver2)
# Yeb-In님 코드

res = []

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

for __ in range(3):
    idx = color.index(input())
    res.append(idx) 

resistance = int(str(r[0]) + str(r[1])) * (10**r[2])
print(resistance)

# ver3)
# 요셉님 코드
reg_color = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
print( (10*reg_color[input()] + reg_color[input()] * 10**reg_color[input()]) )