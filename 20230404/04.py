menu = ( '기본함바가', '치즈함바가', '불고기바가', '와파킹바가')
price = (4000, 4500, 5000, 7000)

for k in range(len(menu)):
    print(k+1, ':', menu[k], ':', price[k])
    
    
# 만약에 메뉴를 추가한다면 list로 만들어 추가한 후 다시 튜플로 가능
# menu.append('새우바가')
# price.append(5500)

lmenu = list(menu)
lprice = list(price)
lmenu.append('새우바가')
lprice.append(5500)

menu = tuple(lmenu)
price = tuple(lprice)
print('메뉴: ', menu)
print('가격: ', price)