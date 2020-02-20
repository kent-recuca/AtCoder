# -*- coding: utf-8 -*-
import math
def main():
    N = int(input())
    ans = []
    for i in range(1,int(math.sqrt(N)+1)):
        if (N % i)==0:
            ans.append((N//i)+i-2)
    print(min(ans))

if __name__ == '__main__':
    main()