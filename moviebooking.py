import random
import imdb
from gmail import mailreceipt
import os.path
import datetime
from datetime import date
from snacks import snacks

now=datetime.datetime.now()
date=date.today() 
day=now.strftime('%a')

def bookmovie():
    ia = imdb.IMDb()
    name=input('ENTER MOVIE NAME: ')
    print()
    print('PLEASE WAIT FOR A MOMENT WHILE WE ACCESS YOUR LOCATION..')
    search = ia.search_movie(name)
    code=search[0].movieID
    print('SELECTING THE NEAREST CINEMA HALL..')
    movie=ia.get_movie(code)
    print()
    print('SUCCESS....')
    print('\n')

    print('BIRLA CINEMAS')
    print(movie,' (',movie['year'],')',sep='')
    print('AVAILABLE TIME SLOTS FOR TODAY')
    flag=0
    while flag==0:
        showtime=['10:00-13:00','13:05-16:05','16:30-19:30','20:00-23:00','23:15-02:15']
        print('10:00-13:00==>0')
        print('13:05-16:05==>1')
        print('16:30-19:30==>2')
        print('20:00-23:00==>3')
        print('23:15-02:15==>4')
        t=input('make choice(0-4): ')
        print()
        if t not in ['0','1','2','3','4']:
            print('INVALID INPUT...TRY AGAIN...')
            print('\n'*2)
        else:
            t=int(t)
            T=showtime[t]
            flag=1
    t1=[]
    for i in range(1,8):
        for j in range(1,8):
            t1.append([i,j])
    random.shuffle(t1)
    
    n=random.randint(1,25)
    t2=[]
    for i in range(len(t1)):
        if i<=n:
            t2.append(t1[i])
        else:
            break

    audnum=random.randint(1,10)
    print('AUDITORIUM NUMBER:',audnum)
    print('            ------------------------------screen------------------------------------')
    print()

    for i in range(1,8):
        print('ROW NO.',i,end='   ')
        for j in range(1,8):
            if [i,j] not in t2:
                print('   O  ',end='     ')
            else:
                print('   *  ',end='     ')
        print()
    print('        ','COLUMN1','COLUMN2','COLUMN3','COLUMN4','COLUMN5','COLUMN6','COLUMN7',sep='    ')
    print()
    print('O: AVAILABLE SEAT')
    print('*: ALREADY BOOKED SEAT')
    print()

    print('PRICE PER SEAT')
    print('Rs. 150: ROW 1 TO ROW 4')
    print('Rs. 250: SILVER(ROW 5)')
    print('Rs. 300: GOLD(ROW 6)')
    print('Rs. 350: PLATINUM(ROW 7)')
    print()
    N=int(input('NUMBER OF SEATS TO BE BOOKED: '))
    print()
    i=0
    b=[]
    price=[]
    while i<N:
        print('BOOKING ',i+1,')',sep='')
        name=input('NAME OF PERSON: ')
        name=name.upper()
        age=int(input('CURRENT AGE: '))
        gender=input('ENTER GENDER(M/F): ')
        gender=gender.upper()
        r=int(input('Enter row number(1-7): '))
        c=int(input('Enter column number(1-7): '))
        if [r,c] not in t2 and [r,c] in t1:
            t2.append([r,c])
            b.append([[r,c],name,age,gender])
            if r<5:
                price.append(150)
            elif r==5:
                price.append(250)
            elif r==6:
                price.append(300)
            else:
                price.append(350)
            print()
            i=i+1
        else:
            print('NO SEAT AVAILABLE FOR THE GIVEN LOCATION...TRY AGAIN...')
            print()
    print('SUCCESS..')
    print()
    m=snacks()
    khana=0
    if m!=[]:
        for j in range(len(m)):
            khana=khana+(m[j][1])*(m[j][2])        
    print()
    print('-------------------------------------')
    print('BOOKING SUCCESSFUL...')
    print('TOTAL BILL IS Rs:',sum(price)+khana)
    print('-------------------------------------')
    print()    
  
    fileout=open('receipt.txt','w')
    list=[]
    list.append('            BIRLA CINEMAS'+'\n')
    list.append('Address: Ghanta Ghar, GT Rd, Block 40'+'\n')
    list.append('Shakti Nagar, Delhi, 110007'+'\n')
    list.append('Telp. 11223344'+'\n'*2)
    list.append('**************************************'+'\n')
    list.append('            CASH RECEIPT'+'\n')
    list.append('**************************************'+'\n')
    for i in range(N):
        list.append('TICKET '+ str(i+1)+'\n')
        list.append('AUDITORIUM '+ str(audnum)+'\n')
        list.append('RECEIPT #: '+ str(random.randint(1000000000000,9999999999999)) + '\n')
        list.append('[' + str(day)+'] ' + str(date) +'\n')
        list.append(T+'\n')
        list.append(str(movie) + ' (' + str(movie['year']) + ')' + '\n')
        list.append('SEAT: ' + str(b[i][0]) + '\n')
        list.append('NAME: '+ b[i][1]+'\n')
        list.append('AGE: '+ str(b[i][2])+'\n')
        list.append('GENDER: '+ b[i][3]+'\n')
        list.append(str(price[i]) + '/-' + '\n')
        list.append('**************************************'+'\n')
    for i in range(len(m)):
        if i==0:
            list.append('SNACKS'+'\n')
        list.append(m[i][0]+': '+str((m[i][1]))+'*'+str((m[i][2]))+' = '+str((m[i][1])*(m[i][2]))+'/-'+'\n')
    if m!=[]:
        list.append('**************************************'+'\n')
    list.append('TOTAL     '+str(sum(price)+khana)+'/-'+'\n'*2)
    list.append('**************************************'+'\n')
    list.append('            THANK YOU!!')
    fileout.writelines(list)
    fileout.close()

    path=os.path.abspath('receipt.txt')
    mailreceipt(path)
    



