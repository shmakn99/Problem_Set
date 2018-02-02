# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:37:27 2018

@author: Manik Sharma
"""

import numpy as np

class search:
    
    def __init__(self,a1,a2):
        # Creating a map from the float array to the second array
        self.map=dict(zip(a1,a2))
        
    def searcher(self,val,acc):   
        # Segregating all the values within the accuracy range
        within = [(self.map[k],np.abs(k-val)) for k in self.map.keys() if np.abs(k-val)-acc<=0]
    
        if len(within)==0:
            # If no value within accuracy range return 0
            return(None)
        else:
            # Else return the value with the least deviation from accuracy
            return(sorted(within, key=lambda x:x[1])[0][0])
        
#Test Case 
a1=np.array([0.2,0.4,0.6,0.9,1.0,1.5,0.3,0.25])
a2=['a','b','c','d','e','f','g','h']

s1=search(a1,a2)

val=0.5
acc=0.2

print (s1.searcher(val,acc))



