def gcf(*args):
    factors = []
    if len(args) < 1:
        return 'lol u stupid?'
    for i in xrange(1, args[0] + 1, 1):
        if args[0] % i == 0:
            factors.append(i)
    output = factors + []
    for i in args:
        for j in factors:
            if not i % j == 0:
                output.remove(j)
    return max(output)


def lcm(*args):
    if len(args) < 1:
        return 'lol u stupid?'
    n = 0
    args = list(args)
    if args[0] < 1:
        args[0] *= -1
    while True:
        n += args[0]
        found = True
        for i in args:
            if i < 0 :
                i = -i
            if not n % i == 0:
                found = False
                break
        if found:
            return n


def pf(arg):
    list = []
    if arg < 2:
        return 'lol u stupid?'
    n = 1
    while True:
        n += 1
        if arg % n == 0 :
            arg /= n
            list.append(n)
            n -= 1
        if arg == 1:
            return list
