import re
import math

x = []
for n in re.findall('\d', str(math.factorial(100))): x.append(int(n))

print sum(x)
