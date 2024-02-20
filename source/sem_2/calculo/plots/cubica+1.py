import itertools
import matplotlib.pyplot  as plt

r = range( -3, 4 )

def values():
    for x in r:
        q = x, f( x )
        print( f"{q[0]},", q[1] )
        yield q

def f( x ):
    return ( x ** 3 ) + 1

X, Y = map( list, itertools.zip_longest( *list( values() ) ) )

xmin = min( X )
xmax = max( X )

ymin = min( Y )
ymax = max( Y )

if xmin > -10:
    xmin = -10
if xmax < 10:
    xmax = 10

if ymin > -10:
    ymin = -10
if ymax < 10:
    ymax = 10

xmax = max( abs( xmin ), abs( xmax ) )
ymax = max( abs( ymin ), abs( ymax ) )

xmax = max( xmax, ymax )
ymax = xmax
xmin = -xmax
ymin = -ymax

#plt.plot( X, Y )
#plt.xlim( -4, 4 )
#plt.ylim( -8, 9 )

# Plot points
fig, ax = plt.subplots( figsize=( 10, 10 ) )

# Set identical scales for both axes
ax.set( xlim=( xmin-1, xmax+1 ), ylim=( ymin-1, ymax+1 ), aspect='equal' )

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position( 'zero' )
ax.spines['left'].set_position( 'zero' )

# Remove top and right spines
ax.spines['top'].set_visible( False )
ax.spines['right'].set_visible( False )

# Draw major and minor grid lines
ax.grid( which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2 )

ax.plot( X, Y )
ax.scatter( X, Y, )

plt.show()
