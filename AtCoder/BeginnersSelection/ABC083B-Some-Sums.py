# -*- coding: utf-8 -*-
def main():
    N,A,B = map(int,input().split())
    out = list()
    for i in range(1,N+1):
        tmp = [int(x) for x in list(str(i))]
        I = sum(tmp)
        if A<=I<=B:
            out.append(i)
    print(sum(out))

if __name__== '__main__':
    main()