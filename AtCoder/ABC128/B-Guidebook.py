# -*- coding: utf-8 -*-
def main():
    N = int(input())
    SP=[list(map(str,input().split())) for i in range(N)]
    for k in range(len(SP)):
        SP[k].append(k)
    for i in range(len(SP)):
        SP[i][1] = int(SP[i][1])
    SP.sort(key=lambda x:(x[0],-x[1]))
    for j in range(len(SP)):
        print(SP[j][2]+1)

if __name__ == '__main__':
    main()