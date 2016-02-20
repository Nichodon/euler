output = 0
for i in xrange(100, 1000, 1):
    for j in xrange(100, 1000, 1):
        if str(i * j) == str(i * j)[::-1] and i * j > output:
            output = i * j
print output