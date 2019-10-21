# coding=utf-8
print([x*x for x in range(1, 11) if x%2 ==0 ])

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [L2.lower() for L2 in L1 if isinstance(L2, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


