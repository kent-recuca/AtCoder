# -*- coding: utf-8 -*-
def main():
    S = list(str(input()))
    S2 = list(reversed(S))
    N = len(S)//2
    ans = 0
    for i in range(N):
        if S[i] != S2[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()