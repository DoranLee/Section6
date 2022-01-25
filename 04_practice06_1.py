n = int(input('정수를 입력하세요 > '))

if n > 0 :
    i = 1
    while i <= n :
        print(f'{i}번째 Hello')
        i += 1
else :
    print('잘못된 입력입니다.')