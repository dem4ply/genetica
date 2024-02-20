import sys
import math
import functools
import collections
import csv
import matplotlib.pyplot  as plt

data = [
	10.9,12.8,14.0,16.4,
	11.1,12.9,14.0,16.5,
	11.2,13.2,14.0,16.5,
	11.5,13.2,14.1,17.0,
	11.5,13.5,14.1,17.5,
	12.0,13.5,14.4,
	12.2,13.7,15.0,
	12.5,13.8,15.0,
	12.8,14.0,15.5,
	12.8,14.0,15.5,

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
y_data = []
histogram_data = []
labels = []
for i in range( class_amount ):
    labels.append( start )
    y_data.append( start )
    end = start + size_class
    end = round( end, 2 )
    labels.append( end )
    data_frecuency = list( d for d in data if ( d >= start and d < end ) )
    absolute_frecuency = len( data_frecuency )
    histogram_data.append( absolute_frecuency )
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

fig, ax = plt.subplots( 1, 1 )

print( histogram_data )
print( y_data )

#ax.bar( y_data, histogram_data, align='center' )
#ax.hist( histogram_data, bins=class_amount )
ax.hist( data, bins=labels )
plt.show()
