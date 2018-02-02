# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:29:35 2018

@author: Manik Sharma

The problem is solved by using a graph element. Elements from each vector with 
< 2 ppm (pars per million, 2e-06) difference are connected by an egde. All the 
connected components are seperated and then filled into the array in the
desired output format.
"""

import networkx as nx
import numpy as np

#'a' is a list of all the float arrays
#Method inputs are the arrays and threshold (taken as 1 for test case but can be changed to 2ppm)
def merger(a,thresh):

    G=nx.Graph()
    
    #Creating the Graph
    
    for i in range(len(a)):
        for j in a[i]:
            G.add_node((j,i))
            
    #Making the edges
    
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for n1 in a[i]:
                for n2 in a[j]:
                    if np.abs(n1-n2)<=thresh:
                        G.add_edge((n1,i),(n2,j))
        
    #Getting the connected components 
    
    con_comp=list(nx.connected_components(G))
    
    fin_m=[[] for i in range(len(a))]
    
    k=1
    
    for comp in con_comp:  
        for ele in list(comp):
            print (ele)
            fin_m[ele[1]].append(ele[0])
           
        for lst in fin_m:
            if len(lst)!=k:
                lst.append(None)
        k+=1
                          
    return(np.array(fin_m))
  
    #Test Case
    
a=[[1,9,15],[5,8,14,20,30],[2,4,10,29]]

print (merger(a,1))