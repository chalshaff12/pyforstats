# -*- coding: utf-8 -*-

import numpy as np
import pickle
import pandas as pd
filename = "source/load.csv"


#manual:
cols = None
data = []
with open(filename) as f:
    for line in f.readlines():
        vals = line.replace("\n", "").split(",")
        if cols is None:
            cols = vals
        else:
            data.append([float(x) for x in vals])
            
d0 = pd.DataFrame(data, columns=cols)

print(d0.dtypes)
print(d0.head())



#numpyloadtext - returns 2D array

d1 = np.loadtxt(filename, skiprows=1, delimiter=",")
print(d1.dtype)

#rows, columns
print(d1[:5, :])


#numpygenfromtext -- named columns are not another dimension, it's just one array, no columns

#dtype=None - figure out which datatypes they should be 
d2 = np.genfromtxt(filename, delimiter=",", names=True, dtype=None)
print(d2.dtype)

#rows, columns
print(d2[:5])

#get jst column A = refer to it by name
#print(d2['A'][:5])


#panda readcsv
d3 = pd.read_csv(filename)

print(d3.dtypes)
print(d3.head())


#pickle
with open("source/load_pickle.pickle", "rb") as f:
    d4 = pickle.load(f)
    print(d4.dtypes)
    print(d4.head())

