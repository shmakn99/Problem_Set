# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:29:35 2018

@author: Manik Sharma

The same principle is applied here each array can contribute more than one node to the
connected component. All these nodes originating form a single array are merged into a 
single node using the function fixer.
"""



import networkx as nx
import numpy as np

G=nx.Graph()

def fixer(lst,lena):
    
    map={}
    
    for i in range(lena):
        map[i]=[]

    for l in lst:
        map[l[1]].append(l[0])
        
    return(map)
    
    

def merger(a,thresh):

    for i in range(len(a)):
        for j in a[i]:
            G.add_node((j,i))
    
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for n1 in a[i]:
                for n2 in a[j]:
                    if np.abs(n1-n2)<=thresh:
                        G.add_edge((n1,i),(n2,j))
        
    
    b=list(nx.connected_components(G))
    
    
    
    b_c=[fixer(i,len(a)) for i in b]
    
    
    fin_m=[[] for i in range(len(a))]
    
    
    for dic in b_c:
        for i in range(len(a)):
            fin_m[i].append(dic[i])
            
    return(np.transpose(np.array(fin_m)))
    
a=[[0.5,8],[1,8.5,5.1,20.1,20.6],[1.5,0.9,4.9,19.9,19.8]]

print (merger(a,1))
