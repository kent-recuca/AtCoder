# -*- coding: utf-8 -*-
def main():
    A,B = map(int,input().split())
    C = A-(B*2)
    if C < 0:
        C = 0
    print(C)

if __name__ == '__main__':
    main()