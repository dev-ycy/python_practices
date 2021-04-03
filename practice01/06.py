# 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
# 각 몇 개로 변환 되는지 작성하시오.

num = int(input("금액: "))

(five_man, num) = divmod(num, 50000)
(one_man, num) = divmod(num, 10000)
(five_chun, num) = divmod(num, 5000)
(one_chun, num) = divmod(num, 1000)
(five_beak, num) = divmod(num, 500)
(one_beak, num) = divmod(num, 100)
(five_sip, num) = divmod(num, 50)
(one_sip, num) = divmod(num, 10)
(five_, num) = divmod(num, 5)
(one_, num) = divmod(num, 1)

print(f"50000원 : {five_man}개")
print(f"10000원 : {one_man}개")
print(f"5000원 : {five_chun}개")
print(f"1000원 : {one_chun}개")
print(f"500원 : {five_beak}개")
print(f"100원 : {one_beak}개")
print(f"50원 : {five_sip}개")
print(f"10원 : {one_sip}개")
print(f"5원 : {five_}개")
print(f"1원 : {one_}개")

