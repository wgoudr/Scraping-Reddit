#organizing_bg_data

import json
from pathlib import Path
#import csv   dont need

#read and load json file into a python list
path = Path(("baldursgate_goty_data.json"))
content_read = path.read_text()
bg_goty_loaded = json.loads(content_read)

#sorting biden and trump counts based on unix time and creating a new list
sorted_bg_and_goty = sorted(bg_goty_loaded, key=lambda key_x: key_x['unix_time'])

data_set = [[],[]]
for i in range(len(sorted_bg_and_goty)):
    bg_xval = sorted_bg_and_goty[i]['bg_count']
    goty_yval = sorted_bg_and_goty[i]['goty_count']
    data_set[0].append(bg_xval)
    data_set[1].append(goty_yval)

"""data_range = len(data_set[0])
for i in reversed(range(data_range)):
    if data_set[0][i] == 0 and data_set[1][i] == 0:
        data_set[0].pop(i)
        data_set[1].pop(i)"""

for row in sorted_bg_and_goty:
    for key, value in row.items():
        print(f"{key}: {value} ", end='')
    print('')

for i in range(len(data_set[0])):
    print(data_set[0][i], data_set[1][i])
   

