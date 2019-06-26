# -*- coding: utf-8 -*-
import fractions
def lcm(x, y):
    return (x*y) // fractions.gcd(x, y)
def main():
    A,B,C,D = map(int,input().split())
    E = lcm(C,D)
    Cc = B // C
    Dd = B // D
    Ee = B // E
    flo = A-1
    Cf = flo // C
    Df = flo // D
    Ef = flo // E
    All = B-(Cc+Dd-Ee)
    Sub = flo-(Cf+Df-Ef)
    print(int(All - Sub))
if __name__ == '__main__':
    main()