# 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
### 못 풀음 ㅜㅜ ###

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

print(s)

result = ''
for i in s:
    if i.startswith("<"):
        pass

    if i == "<":
        for j in range(i):
            print(j)


# i = s.find('<')
# print(i)

result = []
for i in s:
    if i == '<':

    if i == '>':
        continue
    result.append(i)

print(result)
