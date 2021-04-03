# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.


num = int(input("숫자를 입력하세요: "))

if num % 2 == 1:
    result = 0
    for i in range(1, num+1, 2):
        result += i
else:
    result = 0
    for i in range(0, num+1, 2):
        result += i

print(f"결과 값: {result}")