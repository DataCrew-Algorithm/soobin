#BABBA 30840KB / 72ms / 156B

#############이해를 위한 설명##################
# 0 - A                       A : 1 B : 0
# 1 - B                       A : 0 B : 1
# 2 - BA                      A : 1 B : 1
# 3 - BAB                     A : 1 B : 2
# 4 - BABBA                   A : 2 B : 3 
# 5 - BABBABAB                A : 3 B : 5
# 6 - BABBABABBABBA           A : 5 B : 8
# 7 - BABBABABBABBABABBABAB   A : 8 B : 13


#   k       1  2  3  4  5  6  7  ...
# index  0  1  2  3  4  5  6  7  ...
#  A  = [1, 0, 1, 1, 2, 3, 5, 8, ...]
#  B  = [0, 1, 1, 2, 3, 5, 8, 13 ...]

##############################################

k = int(input())

A = [0] * (k+1)            
B = [0] * (k+1)
A[0] = 1

for i in range(1, k+1):
    A[i] = B[i-1]
    B[i] = A[i-1] + B[i-1]

print(A[k], B[k])
