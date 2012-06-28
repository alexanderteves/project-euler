import math

for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 1000):
            if a < b and b < c:
                if (a + b + c) == 1000 and (math.pow(a, 2) + math.pow(b, 2)) == math.pow(c, 2):
                    print 'a : %s | b : %s | c : %s' % (a, b, c)
                    print a * b * c
