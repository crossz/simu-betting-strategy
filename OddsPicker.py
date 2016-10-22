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

game_os_score = numpy.rot90(game_os)
game_os_live = game_os[game_os_score[0] == u'-',:]

print(game_os_live)

# %% pick the odds serie of fav
o1 = numpy.rot90(game_os_live)

odds_hda = o1[2:5,:]
odds_ave = numpy.average(odds_hda, axis=1)

odds_min_index = numpy.argmin(odds_ave)

odds_serie = odds_hda[odds_min_index]

# %%
o2 = odds_serie

