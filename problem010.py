tmp = range(2, 2000001)
primes = []

while True:
    if len(tmp) > 0:
        primes.append(tmp[0])
        tmp = filter(lambda x: x%tmp[0] != 0, tmp)
    else: break

print sum(primes)
