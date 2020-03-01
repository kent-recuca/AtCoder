# -*- coding: utf-8 -*-
def main():
    N,M = map(int,input().split())
    SC = [list(map(int,input().split())) for i in range(M)]
    ans = []
    anst = ''
    for _ in range(N):
        ans.append(-1)
    for j in range(M):
        if ans[SC[j][0]-1] == -1  or ans[SC[j][0]-1] == SC[j][1]:
            ans[SC[j][0]-1] = SC[j][1]
        else:
            print('-1')
            return
    for k in range(N):
        if ans[k] == -1:
            if k == 0 and 2 <= N:
                ans[k] = 1
            else:
                ans[k] = 0
        anst += str(ans[k])
    if len(str(int(anst))) != N:
        print('-1')
        return
    print(int(anst))
if __name__ == '__main__':
    main()