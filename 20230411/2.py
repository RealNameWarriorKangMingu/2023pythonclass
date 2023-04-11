menulist = ['기본햄바가', '치즈햄바가', '불고기바가', '와퍼킹바가']
pricelist = [4000, 4500, 5000, 7000]

# 두 리스트를 튜플이나 딕셔너리로 짝을 만들고 싶을 때에 zip() 함수
tlist = list(zip(menulist, pricelist))
dlist = dict(zip(menulist, pricelist))

print('튜플리스트 = ', tlist)
print('딕셔너리리스트 =', dlist)