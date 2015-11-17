import pandas as pd
import os

basepath = os.getcwd()
datapath = os.path.abspath(os.path.join(basepath, "..", "data", "raw", "ml-100k", "u"))

reviews = pd.read_csv(datapath+'.data', sep='\\t', header=None,
                      names=['userid', 'movieid', 'rating', 'timestamp'])

movies = pd.read_csv(datapath+'.item', sep='|', header=None,
                     names=['movieid', 'title', 'release', 'video',
                              'imdb'] + ['g'+str(i) for i in range(1, 20)])

users = pd.read_csv(datapath+'.user', sep='|', header=None,
                    names=['userid', 'age', 'gender', 'occupation', 'zip'])

reviews_movies = pd.merge(reviews, movies, how='left',
                          on='movieid', sort=False)

reviews_full = pd.merge(reviews_movies, users, how='left',
                        on='userid', sort=False)

# extract year from release date
reviews_full['movieyear'] = reviews_full.release.apply(lambda x: int(x[-4:]) if isinstance(x, str) else x)

# drop unwanted columsn
reviews_full.drop(['timestamp', 'title', 'release',
                   'video', 'imdb', 'occupation', 'zip'], axis=1, inplace=True)

outpath = os.path.abspath(os.path.join(basepath, "..", "data", "prepped", "reviews_100k.csv"))
reviews_full.to_csv(outpath)