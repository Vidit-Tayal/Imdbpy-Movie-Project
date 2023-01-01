def top():
    flag=0
    while flag==0:
        try:
            num=int(input('I WANT TO SEE THE LIST OF TOP n MOVIES, ENTER n: '))
            if num<=0:
                print(abcd) #deliberately creating error
            flag=1
        except:
            print('INVALID INPUT.. TRY AGAIN...')
            print()
        
    print()
    
    print('JUST A MOMENT...')

    import imdb 
    ia = imdb.IMDb()  
    search = ia.get_top250_movies() 

    print()
    print('IMDB: TOP',num,'MOVIES')
    print('----------------------------------------------------------------')
    print('RANK',' RATING',' MOVIE TITLE')
    for i in range(num):
        if i<9:
            print('   ',i+1,'   ',search[i]['rating'],'    ',search[i]['title'],' (',search[i]['year'],')',sep='')
        else:
            print('  ',i+1,'   ',search[i]['rating'],'    ',search[i]['title'],' (',search[i]['year'],')',sep='')
    print('----------------------------------------------------------------')
    print()





