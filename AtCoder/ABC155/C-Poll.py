# -*- coding: utf-8 -*-
from collections import Counter
def main():
    N = int(input())
    S = [input() for i in range(N)]
    c = Counter(S)
    ans = []
    cmax = c.most_common()[0][1]
    ans = [k for k , j in c.items() if j == cmax]
    ans.sort()
    print('\n'.join(ans))
if __name__ == '__main__':
    main()