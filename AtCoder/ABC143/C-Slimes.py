# -*- coding: utf-8 -*-
def main():
    N = int(input())
    S = list(str(input()))
    St = []
    for i in range(N-1):
        if S[i]==S[i+1]:
            continue
        St.append(S[i])
    if S[N-2]==S[N-1]:
        St.append(S[N-2])
    else:
        St.append(S[N-1])
    print(len(St))

if __name__ == '__main__':
    main()