high = 0
value = 0

for x in range(1, 1000000):
    chain = []
    n = x
    while True:
        chain.append(n)
        if n == 1: break
        elif n%2 == 0: n = n/2
        elif n%2 != 0: n = (3*n) + 1
    if len(chain) > high:
        high = len(chain)
        value = x

print value
