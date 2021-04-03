# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.


# 합계 함수
def numsum(*args):
    result = 0
    for i in args:
        result = result + i
    return result

# main
s = input("합할 숫자를 ,로 구분하여 입력하세요: ")
s_list = s.split(',')
nums = []

# 숫자로 변환
for s in s_list:
    nums.append(int(s))

print(numsum(*nums))