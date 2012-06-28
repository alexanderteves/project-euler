tmp = range(2, 120000)
primes = []

while True:
    if len(tmp) > 0:
        primes.append(tmp[0])
        tmp = filter(lambda x: x%tmp[0] != 0, tmp)
        if len(primes) > 10000:
            break
    else: break

print primes[10000]
