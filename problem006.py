import math

print int(math.pow(sum(range(1, 101)), 2) - reduce(lambda x,y: x+y, map(lambda x: math.pow(x, 2), range(1, 101))))
