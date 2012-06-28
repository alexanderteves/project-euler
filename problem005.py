n = 20

while True:
    if n%17 == 0:
        if reduce(lambda x,y: x+y, map(lambda x: n%x, range(1, 21))) == 0: break
    n+=1

print n
