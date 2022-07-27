# 1, 2, 3 더하기
# 숫자에 집착하지 말자 / 갯수에 집중

_list = [1, 2, 4]
for i in range(3, 11):
    _list.append(_list[i-3] + _list[i-2] + _list[i-1])

# print(_list) : [1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504]

import sys

case = int(sys.stdin.readline())

for j in range(case):
    print(_list[int(sys.stdin.readline())-1])

