# -*- coding: utf-8 -*-
import numpy as np
def main():
    mod = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    A = np.array(A, np.int64)
    ans = 0
    for i in range(60):
        bit = np.count_nonzero(A & 1)
        ans += bit * (N - bit) * (2 ** i)
        ans %= mod
        A >>= 1
    print(ans)

if __name__ == '__main__':
    main()