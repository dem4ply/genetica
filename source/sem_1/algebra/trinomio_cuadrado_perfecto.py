import math

def is_a_trinomiun_square_perfect( a, double_ab, b ):
    aa = math.sqrt( a )
    bb = math.sqrt( b )
    print( aa )
    print( bb )
    return (
        double_ab == 2 * aa * bb
        and aa % 1 == 0
        and bb % 1 == 0 )


print( is_a_trinomiun_square_perfect( 36, 96, 64 ) )

print( is_a_trinomiun_square_perfect( 4, 10, 9 ) )
print( is_a_trinomiun_square_perfect( 1, 14, 49 ) )
print( is_a_trinomiun_square_perfect( 81, 180, 100 ) )
print( is_a_trinomiun_square_perfect( 36, 84, 49 ) )
print( is_a_trinomiun_square_perfect( 9, 30, 25) )
print( is_a_trinomiun_square_perfect( 100, 100, 252 ) )
