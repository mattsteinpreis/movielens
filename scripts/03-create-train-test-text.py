import pandas as pd
import os
import scipy.sparse
import imp
import random

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

# create train/test
n = reviews_lil.shape[0]
n_train = int(0.8 * n)
shuffled = range(n)
random.shuffle(shuffled)
train_ind = shuffled[:n_train]
test_ind = shuffled[n_train:]

# convert to dict-like text file
print "writing to text..."
outpath = os.path.abspath(os.path.join(basepath, "..", "data", "prepped", "train.txt"))
fm.write_sparse_to_text(reviews_lil[train_ind], outpath)
outpath = os.path.abspath(os.path.join(basepath, "..", "data", "prepped", "test.txt"))
fm.write_sparse_to_text(reviews_lil[test_ind], outpath)
print 'done.'
