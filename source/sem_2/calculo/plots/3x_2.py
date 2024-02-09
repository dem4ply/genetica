import matplotlib.pyplot  as plt

r = range( -3, 4 )

def f( x ):
    return 3 * x + 2

def values():
    for x in r:
        yield x, f( x )

X, Y = map( list, zip( *list( values() ) ) )

plt.plot( X, Y )
plt.xlim( -4, 4 )
plt.ylim( -8, 9 )
plt.show()
