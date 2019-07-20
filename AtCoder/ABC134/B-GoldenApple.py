# -*- coding: utf-8 -*-
import math
def main():
    N,D = map(int,input().split())
    out = N/(1+D*2)
    print(math.ceil(out))
if __name__ == '__main__':
    main()