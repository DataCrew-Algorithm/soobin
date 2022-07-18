# N과 M(1)
import sys
from itertools import permutations # permutations : 순열

N, M = map(int, sys.stdin.readline().split())

_list = []
for i in range(1,N+1):
    _list.append(i)      
# print(_list) [1, 2, 3, 4]

perm = permutations(_list, M)
# print(list(perm)) = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

for j in perm:
    for k in j: 
        print(k, end=' ')
    print()
    
#######################################################################
# for j in perm:
#     print(j, sep=' ')  : 튜플 괄호 없애는 법 모를 때 잘못된 풀이
