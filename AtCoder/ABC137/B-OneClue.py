# -*- coding: utf-8 -*-
def main():
    K,X = map(int, input().split())
    for i in range(X - K + 1, X + K):
        print(i)

if __name__ == '__main__':
    main()