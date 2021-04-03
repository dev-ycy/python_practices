# 주어진 if 문을 dict를 사용해서 수정하세요.

menu = input('메뉴: ')
price = {
    '오뎅': 300,
    '순대': 400,
    '만두': 500,
}

if menu in price.keys():
    print(f"가격: {price[menu]}")
else:
    print("가격: 0")
