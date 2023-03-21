print('Googudan by Python---')

for num in range(1, 10):
    for dan in range(2, 10):
        print('%2d x%2d = %3d' % (dan, num, dan*num), end = '')
        print('\n')