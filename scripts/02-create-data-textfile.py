import pandas as pd
import os
import scipy.sparse
import imp

fm = imp.load_source('fm', '../lib/movielens-fm.py')

# read csv
basepath = os.getcwd()
datapath = os.path.abspath(os.path.join(basepath, "..", "data", "prepped", "reviews_100k.csv"))
reviews_full = pd.read_csv(datapath, index_col=0)

# make dummy variables
print "making dummies..."
reviews_dummies = pd.get_dummies(reviews_full,
                                 columns=['userid', 'movieid', 'gender'])

# convert to lil_matrix
reviews_lil = scipy.sparse.lil_matrix(reviews_dummies.values)

# convert to dict-like text file
print "writing to text..."
outpath = os.path.abspath(os.path.join(basepath, "..", "data", "prepped", "reviews_dict_100k.txt"))
fm.write_sparse_to_text(reviews_lil, outpath)
print 'done.'
