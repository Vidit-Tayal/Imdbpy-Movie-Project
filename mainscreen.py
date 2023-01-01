#BEFORE RUNNING THE PROGRAM:
    #1 execute: pip install imdbpy 
    #2 ensure that your mysql password is same as the passwd given in 'snacks.py'
    #3 ensure stable internet connection while running the entire program.
    #4 please run the program on command prompt only, not on shell mode.

import time
import os
from moviedetails import details,hi
from moviebooking import bookmovie
from top_chart import top
from bollywoodgame import playgame


flag=0
while flag==0:
    print('================ FILMOPHILE =================')
    print('1. SEARCH FOR A MOVIE/TV-SERIES')
    print('2. TOP CHARTS')
    print('3. BOOK MOVIE TICKETS')
    print('4. DETAILED MOVIE SYNOPSIS')
    print('5. PLAY GAME WITH A FRIEND')
    print('6. EXIT')
    n=input('MAKE CHOICE(1-5): ')
    _=os.system('cls')
    if n=='1':        
        details()
        print()
        
    elif n=='2':
        top()
        
    elif n=='3':
        bookmovie()
        
    elif n=='4':
        print()
        print('READING MOVIE SYNOPSIS IS AN ALTERNATIVE TO WATCHING MOVIES....')
        print()
        print('SPOILER ALERT!!......')
        print()
        print('THIS SECTION CONTAINS SOME SERIOUS SPOILERS OF THE MOVIE....')
        print()
        print('1. YES, PROCEED ANYWAY')
        print('2. NO, I WISH TO GO BACK')
        print()
        choice=input('ENTER CHOICE(1/2): ')
        
        if choice=='1':    
            import imdb
            ia = imdb.IMDb()
            name=input('ENTER MOVIE NAME: ')
            print()
            print('JUST A MOMENT...')
            print()
            search = ia.search_movie(name)
            code=search[0].movieID
            movie=ia.get_movie(code) 

            if 'synopsis' in movie.keys():
                synopsis = movie.data['synopsis']
                print(movie,end=' ')
                hi('series years',movie)
                for i in synopsis:
                    print(i)
            else:
                print("SORRY, WE WERE UNABLE TO FETCH ANY MOVIE WITH THE GIVEN NAME...")
                print('-----------------------------------------------')
        print()

    elif n=='5':
        playgame()
        print('\n')

    elif n=='6':
        print('\n'*5)
        print('THANKS...')
        print('---------------------')
        print('MADE BY:')
        print('VIDIT TAYAL')
        print('DAV SRESHTHA VIHAR')
        print('12A(2020-21)')
        print()
        print('SUPPORTED BY:')
        print("KARUNA MA'AM")
        print('---------------------')
        time.sleep(3)
        flag=1

    else:
        print('INVALID INPUT GIVEN....')
        print('TRY AGAIN...')
        print()
