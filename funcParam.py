# coding=utf-8

def product(*param):
    if len(param) <= 0:
        raise TypeError("Empty input")

    else:
        result = 1
        for n in param:
            result *= n
    return result


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))
