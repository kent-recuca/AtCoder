# -*- coding: utf-8 -*-
def main():
    L,R = map(int,input().split())
    LR = R-L
    M = []
    if L <= 2019 <= R:
        print(0)
        return
    for i in range(LR):
        for j in range(LR):
            M.append(((L+i)*(L+1+j))%2019)
            if ((L+i)*(L+1+j))%2019 == 0:
                print(0)
                return
    print(min(M))
if __name__ == '__main__':
    main()