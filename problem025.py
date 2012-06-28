import re

fib = [1, 1]

while True:
    fib.append(fib[len(fib)-2] + fib[len(fib)-1])
    if len(re.findall('\d', str(fib[-1]))) == 1000: break

print len(fib)
