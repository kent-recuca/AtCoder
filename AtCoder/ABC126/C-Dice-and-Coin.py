# -*- coding: utf-8 -*-
from fractions import Fraction
def main():
    N,K = map(int,input().split())
    countlist = []
    answer = 0
    for i in range(N):
        count = 0
        while i+1 <= K-1:
            i += (i+1)*2
            count +=1
        countlist.append(count)
    for j in countlist:
        answer += Fraction(1,N) * Fraction(1,2)**j
    print(answer)

if __name__ == '__main__':
    main()