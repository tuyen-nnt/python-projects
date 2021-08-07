from itertools import chain
import numpy as np
import csv

writer = csv.writer(open("out.csv", "w"), quoting=csv.QUOTE_NONE)
reader = csv.reader(open("/home/tuyen/Downloads/bao.csv", "r"), skipinitialspace=True)
writer.writerows(reader)

file = "out.csv"

data = np.loadtxt(file, delimiter=',', dtype=str)
data = data.astype('object')

data[1:,0] = data[1:,0].astype(int)
data[1:,3] = data[1:,3].astype(int)
data[1:,6] = data[1:,6].astype(int)

print(type(data[1,0]))

#np.savetxt("np-converter.csv", data, delimiter=",")

with open('np-converter.csv', 'w') as fh:
    writer = csv.writer(fh, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(chain.from_iterable(data))

print(type(data))


# https://pythonguides.com/python-write-array-to-csv/
# https://stackoverflow.com/questions/53168799/writing-a-list-of-numpy-arrays-to-csv

# https://stackoverflow.com/questions/4753704/python-csv-remove-quotes-from-value

# https://stackoverflow.com/questions/31598515/write-numpy-array-to-csv-with-row-indices-and-header/47606787
