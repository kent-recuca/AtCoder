# -*- coding: utf-8 -*-
def main():
    N = int(input())
    d = {}
    ans = 0
    for _ in range(N):
        s = "".join(sorted(list(input())))
        if s in d:
            ans += d[s]
            d[s] += 1
        else:
            d[s] = 1
    print(ans)
if __name__ == '__main__':
    main()