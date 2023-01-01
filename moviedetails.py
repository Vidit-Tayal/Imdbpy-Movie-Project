import imdb

def hi(x,mname):
    if x in mname.keys():
        if x=='runtimes':
            print('# ',x.upper(),': ',mname.data[x][0],' minutes',sep='')
        elif x=='series years' or x=='year':
            print('(',mname.data[x],')',sep='')
        else:
            print('# ',x.upper(),': ',mname.data[x],sep='')
    else:
        if x=='series years':
            hi('year',mname)  

def show(x,mname):
    if x in mname.keys():
        print('# ',x.upper(),': ',sep='',end='')    
        t=list(dict.fromkeys(mname.data[x]))#function to store unique values of a list in the same order as before
        if x=='cast':
            while len(t)>6:
                del t[-1]
        elif x=='distributors':
            while len(t)>2:
                del t[-1]
        
        for i in range(len(t)):
            if i==len(t)-1:
                print(t[i])
            else:
                print(t[i],end=',')


def details():            
    name=input('ENTER FULL NAME OF MOVIE/TV-SERIES: ')
    print()
    print('JUST A MOMENT...')
    print()
    ia = imdb.IMDb()
    search = ia.search_movie(name)    

    if search==[]:
        print('SORRY...NO MOVIE/TV-SERIES FOUND WITH THE GIVEN NAME...')
    else:
        code=search[0].movieID
        mname=ia.get_movie(code)
        print('-----------------------------------------------')
        print('# ',mname.data['kind'].upper(),': ',mname,sep='',end=' ')
        hi('series years',mname)
        hi('rating',mname)
        hi('original air date',mname)
        print()
        show('genres',mname)
        if 'plot' in mname.data.keys():
            print('#','PLOT:',end=' ')
            line=mname.data['plot'][0]
            line=line.split('::')[0]
            print(line)   
            print()
        show('cast',mname)
        show('director',mname)
        show('writer',mname)
        print()
        show('producers',mname)
        show('production companies',mname)
        show('distributors',mname)
        print()     
        if 'box office' in mname.keys():
            for i in mname['box office'].keys():
                print('#',i.upper(),':',mname['box office'][i])
        print()
        show('countries',mname)
        show('languages',mname)
        if 'full-size cover url' in mname.keys():
            print('#','LINK FOR POSTER:',mname['full-size cover url'])
        elif 'cover url' in mname.keys():
            print('#','LINK FOR POSTER:',mname['cover url'])
        hi('runtimes',mname)    
        hi('number of seasons',mname)
        print()
        ia.update(mname,['reviews'])
        if 'reviews' in mname.data.keys():
            print('-----------------------------------------------')
            print('#','REVIEWS:')
            print('    * SPOILER ALERT!!......')
            print('    * REVIEWS SECTION MAY CONTAIN SOME SERIOUS SPOILERS OF THIS ',mname.data['kind'].upper(),'....',sep='')
            print()
            print('       1. YES, PROCEED ANYWAY')
            print('       2. NO, I DONT WISH TO SEE REVIEWS')

            i=0
            choice=input('       ENTER CHOICE(1-2): ')
            while choice=='1':
                print('                                DATE ADDED:',mname.data['reviews'][i]['date'])
                print(mname.data['reviews'][i]['content'])
                i=i+1
                print()
                print('1. SEE ONE MORE REVIEW')
                print("2. NO, THAT'S ENOUGH")
                choice=input('ENTER CHOICE(1-2): ')
            print()    
        if 'rating' in mname.data.keys():
            print('OUR RECOMMENDATION:',end=' ')
            if mname.data['rating']>8.7:
                print('A COMPLETE MASTERPIECE!!  MUST WATCH...')
            elif mname.data['rating']>7.8:
                print('EXCELLENT ',mname.data['kind'].upper(),'...',sep='')
            elif mname.data['rating']>6.5:
                print('GOOD ',mname.data['kind'].upper(),'....',sep='')
            else:
                print('AVERAGE ',mname.data['kind'].upper(),'....',sep='')
    print('-----------------------------------------------')
