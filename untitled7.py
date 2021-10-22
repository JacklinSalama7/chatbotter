# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 09:47:30 2021

@author: okaa
"""


import pickle
with open ("classes.pkl", 'rb') as fin:
    input_data = pickle.load (fin, encoding = 'latin1')

#input_data['X1_test'] = X1


print(input_data)



