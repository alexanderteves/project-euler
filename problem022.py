import re

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
names = re.findall('\w+', open('/tmp/names.txt', 'rb').read())
names.sort()

x = 0

for name in names:
    chars = re.findall('\w{1}', name)
    s = 0
    for char in chars:
        s += a.index(char.lower())+1
    x += (names.index(name)+1) * s

print x
