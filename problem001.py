print reduce(lambda x,y: x+y, filter(lambda x: x%3 == 0 or x%5 == 0, range(0, 1000)))
