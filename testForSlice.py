# coding:utf-8

def trim(s):
    if len(s) == 0:
        return s
    for n in range(len(s)):
        if s[0] == ' ':
            s = s[1:]
        elif s[-1] == ' ':
            s = s[:-1]
        else:
            return s
    return s

print("trim('hello  ')  = ", trim('hello  ') )

print("trim('  hello') = ", trim('  hello') )

print("trim('  hello  ')  = ", trim('  hello  ') )

print("trim('  hello  world  ')  = ", trim('  hello  world  ') )

print("trim('')  = ", trim('')  )

print("trim('    ')  = ", trim('    ') )



if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print(trim('  hello  world  '))
    print('测试失败!')
elif trim('') != '':

    print('测试失败!')
elif trim('    ') != '':

    print('测试失败!')
else:
    print('测试成功!')


