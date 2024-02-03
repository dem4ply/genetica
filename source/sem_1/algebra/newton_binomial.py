import math


ca = 1
xa = 'x'
cb = 4
yb = 'y'

exponent = 7


cca = pow( ca, exponent )
print( f'{cca}{xa}^{exponent}' )


for i in range( 1, exponent ):
    cca = 1
    for ii in range( i ):
        cca *= exponent - ii
    cca = cca // math.factorial( i )
    cca *= pow( ca, exponent - i  ) * pow( cb, i )

    print( f'+ {cca}{xa}^{exponent-i}{yb}^{i}' )

cca = pow( cb, exponent )
print( f'+ {cca}{yb}^{exponent}' )
