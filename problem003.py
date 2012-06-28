tmp = range(2, 10000)
primes = []

while True:
    if len(tmp)-1 > 0:
        primes.append(tmp[0])
        tmp = filter(lambda x: x%tmp[0] != 0, tmp)
    else: break

primes.reverse()

for n in primes:
    if 600851475143 % n == 0:
        print n
        break
