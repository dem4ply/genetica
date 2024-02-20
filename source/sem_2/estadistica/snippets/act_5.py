import sys
import math
import functools
import collections
import csv

data = [
	78,78,82,73,80,86,78,
	68,84,75,85,82,76,80,
	70,87,42,39,49,48,43,
	35,42,34,43,30,34,34,
	41,45,45,43,39,38,29,
]
data.sort()

counter = collections.Counter( data )

min_val = min( data )
max_val = max( data )
amplitude = max_val - min_val
class_amount = math.ceil( math.sqrt( len( data ) ) )
stugess = 1 + 3.322 * math.log( len( data ) )

size_class = amplitude / class_amount

writer = csv.writer( sys.stdout )
comulative_absolute_frecuency = 0
comulative_relative_frecuency = 0
start = min_val
for i in range( class_amount ):
    end = start + size_class
    end = round( end, 2 )
    data_frecuency = list( d for d in data if ( d >= start and d < end ) )
    absolute_frecuency = len( data_frecuency )
    relative_frecuency = absolute_frecuency / len( data )
    relative_frecuency = round( relative_frecuency, 2 )
    comulative_absolute_frecuency += absolute_frecuency
    comulative_relative_frecuency += absolute_frecuency
    writer.writerow( [
        f"{start}, {end}", absolute_frecuency, relative_frecuency,
        comulative_absolute_frecuency, comulative_relative_frecuency ] )
    #print( start, end, absolute_frecuency )
    start = end
    start = round( start, 2 )
