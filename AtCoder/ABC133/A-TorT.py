# -*- coding: utf-8 -*-
def main():
    N,A,B = map(int,input().split())
    NA = N*A
    if NA < B:
        print(NA)
    else:
        print(B)
if __name__ == '__main__':
    main()

