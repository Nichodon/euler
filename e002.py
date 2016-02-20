v1, v2 = 1, 2
output = 2
while v2 <= 4000000:
    v1, v2 = v2, v1 + v2
    if v2 % 2 == 0:
        output += v2
print output