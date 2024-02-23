import itertools
import matplotlib.pyplot  as plt

r = range( -5, 6 )

def values():
    for x in r:
        q = x, f( x )
        print( q[0], ',', q[1] )
        yield q

def f( x ):
    return x ** 3

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
#ax.set( xlim=( xmin-1, xmax+1 ), ylim=( ymin-1, ymax+1 ), aspect='equal' )

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position( 'zero' )
ax.spines['left'].set_position( 'zero' )

# Remove top and right spines
ax.spines['top'].set_visible( False )
ax.spines['right'].set_visible( False )

# Create 'x' and 'y' labels placed at the end of the axes
ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

# Draw major and minor grid lines
ax.grid( which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2 )

ax.plot( X, Y )

#horizontal
ax.plot([-3, 0], [f(-3), f(-3)], c='green', ls='--', lw=1.5, alpha=0.5)
ax.plot([0, 3], [f(3), f(3)], c='green', ls='--', lw=1.5, alpha=0.5)
#vertical
ax.plot([-3, -3], [0, f(-3)], c='grenn', ls='--', lw=1.5, alpha=0.5)
ax.plot([3, 3], [0, f(3)], c='green', ls='--', lw=1.5, alpha=0.5)

ax.scatter( X, Y, )

plt.show()
