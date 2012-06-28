from decimal import Decimal
import math
import re

x = []
for n in re.findall('\d', str(Decimal(math.pow(2, 1000)))): x.append(int(n))

print sum(x)
