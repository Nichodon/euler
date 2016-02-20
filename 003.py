n = 1
arg = 600851475143
output = 0
while arg != 1:
    n += 1
    if arg % n == 0 :
        arg /= n
        if n > output:
            output = n
        n -= 1
print output