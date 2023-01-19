from math import*
import random
from random import choice
from re import*
import string
import sys
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
login1=['user1','user2','user3']
passw1=['123','345','567']

#with open('file.txt','r') as base:
#    data=base.readlines()
#users1={}
#for user in data:
#    name=user.split()[1]
#    password=user.split()[0]
#    users1[name]=password
   

#logins=users1.keys()
#def get_data(passw)->tuple:
#    global users1
#    logins=users1.keys()
#    user[logins]=passw
#    return login,passw

#def add_user(passw):
#    data:tuple=get_data(passw)
#    with open('file.txt','r+') as base:
#        base.write(data[0]+""+data[1]+'\n')


def users(a:int)->any:
    user=" "
    for i in range(1):
        t=choice(string.ascii_letters)
        alpha=choice([1,2,3,4,5,6,7,8,9])
        #alpha=choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z])
        t_alpha=[t,str(alpha)]
        #t_alpha=[t,int(alpha)]
        user+=choice(t_alpha)
        
        return user
def password(b:int):
    pass1=" "
    for i in range(b):
        p=choice(string.digits)
        dig=choice([1,2,3,4,5,6,7,8,9])
        #dig=choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z])
        p_dig=[p,str(dig)]
        pass1+=choice(p_dig)
        while True:
            b=str(b)
            if len(b)<4:
                print('simple password')
            while True:
                if len(b)>=4:
                    print('you have registered!')
                    #sys.exit()
                return b
                
def log(login:str,password:str):
    while login==str(login):
        if login in login1:
            login1.append(login)
            if  password in passw1:
                passw1.append(password)
                print(f'Hi there {login}')
            #elif log==login1 and log==passw1:
            #    print('there is a user with this username')
                break
                return log





