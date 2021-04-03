# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'
print('원본 경로명 >> ', s)

s_list = s.split('/')[1:]
print('실행결과 1 >> ' , s_list)

t = '/'.join(s_list)
print('실행결과 1 >> ' + '/' + t)

