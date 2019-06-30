    # -*- coding: utf-8 -*-
def main():
    N = int(input())
    W = list(map(int,input().split()))
    ABS = list()
    for i in range(N):
        MAXs = 0
        MINs = 0
        for j in range(len(W)):
            if i > j:
                MAXs += W[j]
            else:
                MINs += W[j]
        ABS.append(abs(MAXs-MINs))
    print(min(ABS))

if __name__ == '__main__':
    main()