# 3-1
# 다음 문자열을 모든 소문자를 대문자로 변환하고,
# 문자 ',', '.','\n'를 없앤 후에 중복없이 각 단어를 순서대로 출력하세요.

# 3-2
# 각 단어의 빈도수도 함께 출력해 보세요

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

# 3-1
# s_list = s.split()
# t_list = []

# for i in s_list:
#     i.strip()
#     i = i.replace(",", "").replace(".", "")
#     t_list.append(i.upper())
#
# print(t_list)
# t_set = list(set(t_list))
# t_set.sort()
# print(t_set)

# --------------
# 3-1

s_list = s.split()
t_list = []
for i in s_list:
    i.strip()
    i = i.replace(",", "").replace(".", "")
    t_list.append(i.upper())

t_list.sort()
results = {}

for i in t_list:
    if i in results.keys():
        results[i] += 1

    elif i not in results.keys():
        results[i] = 1

for key, value in results.items():
    print(f'{key} : {value}')