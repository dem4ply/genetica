import matplotlib.pyplot  as plt

def f( x ):
    return 3 * x + 2

def values():
    for x in range( -3, 3 ):
        yield x, f( x )

X = []
Y = []
for v in values():
    X.append( v[0] )
    Y.append( v[1] )

plt.plot( X, Y )
plt.xlim( -4, 4 )
plt.ylim( -8, 9 )
plt.show()
