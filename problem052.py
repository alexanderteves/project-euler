import re

def splitInt(i):
    l = re.findall('\d', str(i))
    l.sort()
    return l

n = 1
while True:
    if splitInt(n) == splitInt(n*2):
        if splitInt(n) == splitInt(n*3):
            if splitInt(n) == splitInt(n*4):
                if splitInt(n) == splitInt(n*5):
                    if splitInt(n) == splitInt(n*6):
                        break
    n += 1

print n
