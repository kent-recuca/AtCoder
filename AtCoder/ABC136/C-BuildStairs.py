# -*- coding: utf-8 -*-
def main():
    N = int(input())
    H = list(map(int,input().split()))
    H.reverse()
    for i in range(N):
        if i != N-1:
            if H[i]>=H[i+1]:
                continue
            if (H[i+1]-H[i])==1:
                H[i+1]=H[i+1]-1
            else:
                print('No')
                return
    if H[N-1]<=H[N-2] or (H[N-1]-H[N-2]==1):
        print('Yes')
        return
    else:
        print('No')
        return
if __name__ == '__main__':
    main()