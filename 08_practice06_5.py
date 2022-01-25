n = 1
while n <= 100 :
    if n % 10 == 0 :
        print(n)   # end = '\n'
    else :
        print(n, end='\t\t')
    n += 1

n = 1
str = ''
while n <= 100 :
    str += f'{n}\t\t'
    if n % 10 == 0 :
        str += '\n'
    n += 1
print(str)
