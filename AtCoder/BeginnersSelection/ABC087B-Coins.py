# -*- coding: utf-8 -*-
def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    count = 0
    for i in range(A+1):
        for j in range(B+1):
            for k in range(C+1):
                z = 500*i + 100*j + 50*k
                if z == X:
                    count += 1
    print(count)
if __name__ == '__main__':
    main()
