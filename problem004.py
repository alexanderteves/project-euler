import re

def intReverse(i):
    digits = re.findall('\d{1}', str(i))
    digits.reverse()
    s = ''
    for n in digits: s += n
    return int(s)

numbers = range(100, 1000)
palindromes = []

for x in numbers:
    for y in numbers:
        if x*y == intReverse(x*y): palindromes.append(x*y)

palindromes.sort()

print palindromes[-1]
