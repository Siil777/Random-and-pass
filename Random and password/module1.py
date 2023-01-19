from math import*
import random
from random import choice
from re import*
import string

def users(a:int):
    user=" "
    for i in range(a):
        t=choice(string.acii_letters)
        alpha=choice([1,2,3,4,5,6,7,8,9])
        #alpha=choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z])
        t_alpha=[t,str(alpha)]
        user+=choice(t_alpha)
        print(alpha)
        return user
