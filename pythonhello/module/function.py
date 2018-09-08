'''
Created on Feb 9, 2018

@author: gongyo
'''
colors = ["red", 'yellow']
colors.append("black")


def compare(c1="str", c2="str"):
    return c1 < c2


compare2 = lambda c1, c2: (c1 < c2);
    
colors.sort(cmp=compare2, key=None, reverse=False)
