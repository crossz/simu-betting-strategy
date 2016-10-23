# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 17:29:36 2016

@author: Zheng
"""

# %% load data
import numpy
import pickle

game_data = pickle.load(open('game_data.p', 'rb'))


# %% pick live odds sets

#for i in range(20):

i = 14

game_os = game_data[i].odds_sets
game_os_score = game_os[:,4]
game_os_live = game_os[game_os_score == u'-',:]

print(game_os_live)

# %% pick the odds serie of fav
odds_hda = game_os_live[:,0:3]
odds_ave = numpy.average(odds_hda, axis=0)
odds_min_index = numpy.argmin(odds_ave)
odds_serie = odds_hda[:,odds_min_index]

print(odds_serie)

# %%
p1 = 1/odds_serie
g1 = numpy.gradient(p1)

## test numpy.gradient
for i in range(len(p1)):
    if i == 0:
        gt = p1[1] - p1[0]
    elif i == len(p1)-1:
        gt = p1[len(p1)-1] - p1[len(p1)-2]
    else:    
        gt = (p1[i+1] - p1[i-1])/2

    print("pi={:.5f} -> g={:.5f} | gi={:.5f}".format(p1[i], gt, g1[i]))
    

