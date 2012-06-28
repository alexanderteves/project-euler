fib = [0, 1]

while True:
    if fib[len(fib)-1] < 4000000: fib.append(fib[len(fib)-2] + fib[len(fib)-1])
    else: break

print reduce(lambda x,y: x+y, filter(lambda x: x%2 == 0, fib))
