# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:36:08 2018

@author: Manik Sharma
"""

import re

def extractor(s):

    a= (re.findall('\D+\(',s))
    b= (re.findall('\([A-Z|a-z]',s))
    c= (re.findall('[0-9]{2}:',s))
    d= (re.findall(':[0-9]',s))
    
    ret=[]
    
    ret.append(a[0].strip('('))
    
    if len(b)>0:
        ret.append(b[0].strip('('))
    else:
        ret.append('')
    
    for i in range(len(c)):
        ret.append(c[i].strip(':'))
        ret.append(d[i].strip(':'))
    
    return ret

#TestCase
s='TG(18:0/18:0/18:0)'
print (extractor(s))