# -*- coding: utf-8 -*-
def main():
    N,A,B = map(int,input().split())
    ans0 = N//(A+B)
    ans1 = A*ans0
    ans2 = (N-(A+B)*ans0)
    ans1 += min(ans2,A)
    print(ans1)
if __name__ == '__main__':
    main()