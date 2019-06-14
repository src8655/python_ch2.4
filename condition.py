
# if ~ else
a = 10
if a > 5:
    print('big')
else:
    print('small')

# if ~ elif ~ else
n = -2
if n > 0:
    print('양수')
elif n < 0:
    print('음수')
else:
    print('0')

# 삼항연산자
# 자바에서는
# a > 5 ? 'big' : 'small'
print('big' if a > 5 else 'small')
