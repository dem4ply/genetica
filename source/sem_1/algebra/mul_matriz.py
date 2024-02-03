a = [
    [ 2, 4, 1 ],
    [ 0, 1, -2 ],
]

b = [
    [ 3, 0, 1, -1 ],
    [ -1,3, 1, 2 ],
    [ 4, 0, 3, -2 ],
]

c = [
]

assert len( a[0] ) == len( b )

for i in range( len( a[0] ) ):
    s = 0
    c.append( [] )
    for j in range( len( b ) ):
        print( i, j )
        try:
            s += a[ j ][ i ] * b[ i ][ j ]
        except:
            import pdb
            pdb.set_trace()
    print( 'fd' )
    c[i].append( s )

for i in range( len( c ) ):
    for j in range( len( c[0] ) ):
        print( c[i][j] )
