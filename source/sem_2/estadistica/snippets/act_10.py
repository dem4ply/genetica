import math
import functools
import collections

data = [
	12.03,
	11.98,
	12.02,
	11.98,
	11.95,
	12.02,
	11.98,
	12.01,
	11.96,
	11.95,
]
data.sort()

old_standard_deviation = 0.05

mean = sum( data ) / len( data )
median = data[ len( data ) // 2 ]
mode = collections.Counter( data ).most_common(1)

print( f"* media = {mean}" )
print( f"* mediana = {median}" )
print( f"* moda = {mode}" )

variance = sum( pow( d - mean, 2 ) for d in data ) / len( data )
standard_deviation = math.sqrt( variance )
range_var = max( data ) - min( data )

print( f"* varianza = {variance}" )
print( f"* desviacion estandar = {standard_deviation}" )
print( f"* rango = {range_var}" )

improment = old_standard_deviation - standard_deviation
print()
print( f"mejora por {improment}" )
