# -*- coding: utf-8 -*-
def main():
    answer = ''
    N,K = map(int,input().split())
    S = list(input())
    print(N,K,S)
    if S[K-1] == 'A':
        S[K-1] = 'a'
    elif S[K-1] == 'B':
        S[K-1] = 'b'
    elif S[K-1] == 'C':
        S[K-1] = 'c'
    for s in S:
        answer += s
    print(answer)

if __name__ == '__main__':
    main()

