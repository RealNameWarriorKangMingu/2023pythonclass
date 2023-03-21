import random

gnum = 0

while True :
    com = random.randrange(3)
    user = int(input('가위 0 바위 1 보 2 선택 : '))
    if user == 0 or user == 1 or user == 2:
        print('user = %d, com = %d' % (user, com))
        if user == com :
            print('비겼습니다!')
        elif (user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1) :
            print('이겼습니다!')
        else :
            print('패배했습니다!')
    else:
        break
        
    gnum += 1
    
print("입력한 횟수는 %d번입니다." % gnum)
