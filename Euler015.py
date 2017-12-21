import time

def lattice_paths(k):
    if k == [0,0]:
        return 1
    if k == [12,12]:
        return 2704156
    paths = 0
    if k[0]>0:
        paths+= lattice_paths([k[0]-1,k[1]])
    if k[1]>0:
        paths+=lattice_paths([k[0],k[1]-1])
    return paths
start = time.time()
k = lattice_paths([5,5])
elapsed = (time.time() - start)
print "result %s returned in %s seconds." % (k,elapsed)