# -*- coding: utf-8 -*-
def main():
    N,L = map(int,input().split())
    taste = []
    ABS = []
    for i in range(N):
        taste.append(L+i+1-1)
        #print(taste)
    for j in taste:
        ABS.append(abs(j))
        #print(ABS)
    taste.pop(ABS.index(min(ABS)))
    print(sum(taste))

if __name__ == '__main__':
    main()
