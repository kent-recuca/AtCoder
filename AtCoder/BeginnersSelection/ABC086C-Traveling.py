# -*- coding: utf-8 -*-
def main():
    N = int(input())
    txy = [list(map(int,input().split())) for i in range(N)]
    for j in range(N):
        t = txy[j][0]
        xy = abs(txy[j][1])+abs(txy[j][2])
        if t >= xy and (t%2)==(xy%2):
            continue
        else:
            print('No')
            return
    print('Yes')
if __name__ == '__main__':
    main()
