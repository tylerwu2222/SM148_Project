import pandas as pd
import numpy as np

# location processing
from geopy import geocoders  

import multiprocessing as mp
from multiprocessing import Pool, Array, Lock
# from time import time
from joblib import delayed, Parallel

# all_data = pd.read_csv('complete_data/complete_data_sentiment.csv')
# all_data.head()

# returns coordinates given location
def get_coords2(i,loc,gn):
    if i %3 == 0:
        print('location',i,':',loc)
    try:
        location = gn.geocode(loc,exactly_one=False)
        coords = location[0][1]
        # print(coords)
    except:
        coords = (None,None)
    return coords

pool = mp.Pool()
# NUM_CPUS=8
# gn = geocoders.GeoNames(username='tylerwu')
# unique_locs = all_data.location.unique()
# index = range(0,len(unique_locs))
# # index[:3]
# coord_dict = [pool.apply(get_coords2, args=(i, unique_locs[i], gn)) for i in index[:32]] # mp package
# # coord_dict = Parallel(n_jobs=NUM_CPUS)(delayed(get_coords2)(i,unique_locs[i],gn) for i in index[:10]) #joblib package
# # coord_dict = {unique_locs[i]:get_coords2(i,unique_locs[i], gn) for i in index[:10]} # old-fashioned
# # # pool.close()
# coord_dict

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))