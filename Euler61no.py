tri,sq,pen,hexa,hep,octa = set(),set(),set(),set(),set(),set()
for n in range(1,200):
    tri.add(n*(n+1)/2)
    sq.add(n*n)
    pen.add(n*(3*n-1)/2)
    hexa.add(n*(2*n-1))
    hep.add(n*(5*n-3)/2)
    octa.add(n*(3*n-2))
for trin in tri:
    if len(str(trin)) == 4:
        for x in range(10,100):
            sqn = int(str(trin)[-2:]+str(x))
            if sqn in sq:
                for v in range(10,100):
                    penn = int(str(sqn)[-2:]+str(v))
                    if penn in pen:
                        for z in range(10,100):
                            hexan = int(str(penn)[-2:]+str(z))
                            if hexan in hexa:
                                for q in range(10,100):
                                    hepn = int(str(hexan)[-2:]+str(q))
                                    if hepn in hep:
                                        octan = int(str(hepn)[-2:]+str(trin)[:2])
                                        if octan in octa:
                                            print "solution to Euler 61 is:", trin+sqn+penn+hexan+hepn+octan
                                        else:
                                            print "no octa"
                                    else:
                                        print "no hep"
                            else:
                                print "no hexa"
                    else:
                        print "no penn"
            else:
                print "no sq"
                        