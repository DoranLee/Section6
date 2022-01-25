# set에 5개의 정수가 들어갈 때까지 입력하시오.
n = set()

while len(n) != 5 :
    num = int(input('0부터 9 사이의 정수 입력 > '))
    if 0 <= num <= 9 :
        n.add(num)
print('모두 입력되었습니다.')
print('입력된 값은 {}입니다.'.format(n))

# list, in(not in) 이용하여 풀어보기
# if num not in n :