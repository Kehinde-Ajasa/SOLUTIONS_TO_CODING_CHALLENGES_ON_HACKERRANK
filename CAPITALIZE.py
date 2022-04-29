def solve(s):
    b = ''
    k = (s.split(' '))
    for i in k:
        n = i[:1].upper()
        n += i[1:]
        b += f'{n} '
    return(b)
s = input('Enter your desired words: ')

print(solve(s))
