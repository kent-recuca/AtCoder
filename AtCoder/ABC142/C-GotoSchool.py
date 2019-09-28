# -*- coding: utf-8 -*-
import numpy as np
def main():
    N = int(input())
    A = list(map(int,input().split()))
    An = np.argsort(A)
    for i in An:
        print(i+1,end = " ")
if __name__ == '__main__':
    main()