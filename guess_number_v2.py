'''
1.Random module genrate 5 digit number _ _ _ _ _
2.User get 10 chance to input
3.After every input pc tell user how many number is in correct place and how many number is correct

Important 
1.For easy mode no number is repeted
'''
import random
def n_dif_num(n):
    '''
    1. Return n th digit non repitive number
    2. Return string not integer 
    3. If number start with zero(0) like 034 or 0234 \'int()\' will conver it into 34 and 234 
    '''
    num=''
    for i in range(n):
        
        while True:
            test=str(random.randint(0,9))
            if not test in num:
                num += test
                break
    return num
      

num=n_dif_num(5)
lis=list(num)

for i in range(10):
    print(i+1,'.')
    pos=0
    corr=0
    user=input("Enter 5 digit number: ")
    if user.isalnum() and not user.isdigit() or int(user)<10000 or int(user) >99999:
        print(f"Invalid Input {user}")
        user=input("Enter any 5 digit number or you will loss the game: ")
        if user.isalnum() and not user.isdigit() or int(user)<10000 or int(user) >99999:
            print(f"Invalid Input {user}")
            break
    #####imagining 5 digit number####################
    lis2=list(user)
    for i in range(5):
        if lis2[i] in lis:
            corr+=1
        if lis[i]==lis2[i]:
            pos+=1
    
    if pos==5:
        print(f"Congratulation {user} is correct answer")
        break            
    
    print(f'There are {corr} correct digit\n{pos} placed in correct position\n')
else:
    print(f"you lose number was {num}")    
        
   


