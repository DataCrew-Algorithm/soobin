# 피보나치수 2

# 방법1

from tkinter import N


n = int(input())

fi = [0] * (n+1)
fi[1] = 1

for i in range(2, n+1):
    fi[i] = fi[i-1] + fi[i-2]

print(fi[n])

# 방법2

fi = [0] * (n+1)
fi[1] = 1

n = int(input())

for i in range(2, n+1):
    fi[i] = fi[i-1] + fi[i-2]

print(fi[n])