# -*- coding: utf-8 -*-
def main():
    out = 0
    s1,s2,s3 = input()
    ss = []
    ss.extend([s1,s2,s3])
    for i in ss:
        if i == "1":
            out +=1
    print(out)
if __name__ == '__main__':
    main()