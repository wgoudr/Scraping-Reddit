#organizing_bg_data

# data or processed and organized chronologically into a list of 2 lists. 
# Each list is the set x and y. this lists will be used in the regression.

import json
from pathlib import Path

# read and load json file into a python list
path = Path(("baldursgate_goty_data.json"))
content_read = path.read_text()
bg_goty_loaded = json.loads(content_read)

# sorting bg3 and goty based on unix time and creating a new list
# this is needed because the data is not in chronological order
sorted_bg_and_goty = sorted(bg_goty_loaded, key=lambda key_x: key_x['unix_time'])

# creating a data set that will be used in the regression model 
# this list only needs two sets of data. The first set of data, which
# is the baldur's gate 3 count, will be the independent value (x) and
# the game of the year count, is the second set of data and is the 
# dependent value (y)
# both sets of data are 1 to 1 and order by chronological time
data_set = [[],[]]

for i in range(len(sorted_bg_and_goty)):
    bg_xval = sorted_bg_and_goty[i]['bg_count']
    goty_yval = sorted_bg_and_goty[i]['goty_count']
    data_set[0].append(bg_xval)
    data_set[1].append(goty_yval)

# this is only need to see if anything goes wrong. Not important
for row in sorted_bg_and_goty:
    for key, value in row.items():
        print(f"{key}: {value} ", end='')
    print('')

for i in range(len(data_set[0])):
    print(data_set[0][i], data_set[1][i])
   

