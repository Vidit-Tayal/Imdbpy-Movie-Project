#name of the game is bollywood

from moviedetails import show,hi
import imdb
import time
import os
import getpass

    
def subset(x,y):
    for i in x:
        if i in y:
            flag=1
        else:
            flag=0
            break
    if flag==0:
        return 'no'
    else:
        return 'yes'


def get_hint(hints,mname):
    if hints==0:
        hi('original air date',mname)
        show('languages',mname)
        if 'plot' in mname.data.keys():
            print('#','PLOT:',end=' ')
            line=mname.data['plot'][0]
            line=line.split('::')[0]
            print(line)   
        
    elif hints==1:
        show('genres',mname)
        show('director',mname)        
    else:
        show('cast',mname)

def playgame():
    flag=0
    while flag==0:
        p = getpass.getpass(prompt='ENTER FULL NAME OF MOVIE(ENSURE THAT YOUR FRIEND DOES NOT SEE YOUR KEYBOARD WHILE TYPING): ')
        print()
        print('JUST A MOMENT...')
        print()
        ia = imdb.IMDb()
        search = ia.search_movie(p)

        if search==[]: 
            print('SORRY...NO SUCH MOVIE WITH THE GIVEN NAME...')
            time.sleep(2)
            _=os.system('cls')
            
        
        else:
            code=search[0].movieID
            mname=ia.get_movie(code)
            if mname.data['kind'].upper()!='MOVIE':
                print('SORRY...NO SUCH MOVIE WITH THE GIVEN NAME...')
                time.sleep(2)
                _=os.system('cls')
            else:
                flag=1
        

    
    _=os.system('cls')
    movie=str(mname).upper()
    lt=movie.split()
    count=0
    lt=list(set(lt))
    t1=[]
    for i in lt:
        for j in i:
            if j not in t1:
                count=count+1
                t1.append(j)        
    bolly='BOLLYWOOD'
    health=len(bolly)

    hints=0
    t=['A','E','I','O','U']
    print('GUESS THE MOVIE!!')
    print('=========================================================')
    while health!=0:
        print('[',bolly,']')
    
        for i in movie:
            I=i.upper()
            if I in t:
                print(I,end=' ')
            elif I==' ':
                print(I,end='   ')
            else:
                print('_',end=' ')
        print('\n')   
    
        if health>1 and 3-hints>=1:
            print('# TAKE HINT BY CONSUMING A HEALTH (',3-hints, ' HINTS REMAINING) ??',sep='')
            choice=input('  ENTER CHOICE(Y/N): ')
            if choice in ['Y','y','YES','yes']:
                bolly=bolly[1:]
                print('  ---------------------------------------------------')
                get_hint(hints,mname)
                hints=hints+1
                print('  ---------------------------------------------------')
            
        guess=input('ENTER GUESS: ').upper()       
        while guess==' ' or guess=='':
            print('INVALID INPUT.. ENTER AGAIN...')
            guess=input('ENTER GUESS: ').upper()
        
        
        if guess in movie:
            print('GOOD...')
            print('=========================================================')
            t.append(guess)
            if subset(t1,t)=='yes':
                print('BRAVO! YOU WON:',movie)
                break
        else:
            print('WRONG ATTEMPT...')
            print('=========================================================')
            bolly=bolly[1:]
        health=len(bolly)

    else:
        print('BETTER LUCK NEXT TIME:',movie)
