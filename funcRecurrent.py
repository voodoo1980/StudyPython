# coding:utf-8

def recurrent(n):
    if n == 1:
        return 1
    else:
        return n * recurrent(n-1)


def move(n, a, b, c):
    if n == 1:
        print(a, "===>", c)
    else:
        move(n-1, a, c, b)
        print(a, "===>", c)
        move(n-1, b, a, c)


#aram = int(input("Input param: "))
#print("Run recurrent function: recurrent + ", param,  recurrent(param))


move(5, 'a', 'b', 'c')