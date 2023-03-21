import random
# randrange(0, 4) : 0 ~ 3 까지 무작위 수 만듦
trip = random.randrange(0, 4)
if trip == 0 :
    print('제주도로 고')
elif trip == 1 :
    print('사이판으로 고')
else :
    print('하와이로 고')