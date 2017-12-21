import itertools, collections
cubes=collections.defaultdict(list)
for i in itertools.count(1):
    k = cubes[''.join(sorted(str(i**3)))]
    k.append(i)
    if len(k)==5:
        print "Solution to euler 62:",k[0]**3
        break