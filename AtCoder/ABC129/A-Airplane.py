# -*- coding: utf-8 -*-
def main():
    P,Q,R = map(int,input().split())
    X = list()
    XX = 9999999
    X.append(P+Q)
    X.append(P+R)
    X.append(Q+R)
    #print(X)
    for i in X:
        if XX > i:
            XX = i
    print(XX)
if __name__ == '__main__':
    main()

