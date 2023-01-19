from module90 import*
#from module90 import users
login1=['user1','user2','user3']
passw1=['123','345','567']

while True:
  
    print('would you like to register [1], login [2] exit [0]?')
    a=input('action:')
    if a.isalpha():
        print('only numerous')
    if a.isdigit():
        a=int(a)
    if a==1:
       a=users(str(input('username:')))
       
       b=password(str(input('password:')))
    elif a==2:
        login=log(input('username:'),input('password:'))
    elif a==0:
        print('until next time')
        break

        






