# -*- coding: utf-8 -*-
import math
def main():
    N,K = map(int,input().split())
    num = 0
    while True:
        if (K**(num-1))<= N < (K**num):
            print(math.ceil(num))
            break
        num+=1
if __name__ == '__main__':
    main()
