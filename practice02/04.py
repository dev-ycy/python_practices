# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요.
# 1부터 99까지만 실행하세요.

count = 0
for i in range(1, 100):
    i = str(i)
    count = i.count('3') + i.count('6') + i.count('9')
    if count > 0:
        print(i, '짝'*count)
    else:
        continue