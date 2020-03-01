    # -*- coding: utf-8 -*-
def main():
    A = [list(map(int,input().split())) for i in range(3)]
    N = int(input())
    B = [int(input()) for i in range(N)]
    for j in B:
        for k in range(3):
            for l in range(3):
                if j == A[k][l]:
                    A[k][l] = -1
    A1 = A[0]
    A2 = A[1]
    A3 = A[2]
    if A1.count(-1)==3 or A2.count(-1)==3 or A3.count(-1)==3:
        print('Yes')
        return
    for m in range(3):
        if A1[m] ==-1 and A2[m] == -1 and A3[m] == -1:
            print('Yes')
            return
    if A1[0]==-1 and A2[1]==-1 and A3[2]==-1:
        print('Yes')
        return
    if A1[2]==-1 and A2[1]==-1 and A3[0]==-1:
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()