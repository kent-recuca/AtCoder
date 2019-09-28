# -*- coding: utf-8 -*-
import fractions

def main():
    A,B = map(int,input().split())
    C = fractions.gcd(A,B)
    Cn = prime_factorize(C)
    Cn = list(set(Cn))
    print(len(Cn)+1)

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

if __name__ == '__main__':
    main()
