# -*- coding: utf-8 -*-
def main():
    N = int(input())
    H = list(map(int,input().split()))
    cnt = 0
    flg = 0
    for i in range(N):
        if cnt >= N-i:
            print(cnt)
            return
        if flg!=0:
            if i==flg:
                flg=0
            else:
                continue
        tmp=0
        for j in range(i,N-1):
            if H[j]>=H[j+1]:
                tmp+=1
            else:
                flg=j+1
                break
        if cnt < tmp:
            cnt=tmp
    print(cnt)
if __name__ == '__main__':
    main()