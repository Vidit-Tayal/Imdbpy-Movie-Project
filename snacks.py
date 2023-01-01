def fillspace(string,space):
    print(string,' '*(space-len(string)),sep='',end='')

def listprint(t):
    fillspace(str(t[0]),5)
    fillspace(t[1],20)
    fillspace(str(t[2]),6)
    print(t[3],end='')

import mysql.connector as abc
mc=abc.connect(host = 'localhost',user='root',passwd='dav2020',charset='utf8')
cursor=mc.cursor()

def snacks():
    print('SNACKS')
    print('------------------------------------------')
    print('PID',' PRODUCT','           PRICE','DESCRIPTION')
    try:
        cursor.execute('create database snacks')        
    except:
        cursor.execute('drop database snacks')
        cursor.execute('create database snacks')
        
    cursor.execute('use snacks')     
    cursor.execute('create table snacks(PID INT PRIMARY KEY,PRODUCT VARCHAR(30), PRICE INT, DESCRIPTION VARCHAR(80));')
    cursor.execute('INSERT INTO snacks VALUES(1, "POPCORN", 150,"SMALL")')
    cursor.execute('INSERT INTO snacks VALUES(2, "POPCORN", 250,"MEDIUM")')
    cursor.execute('INSERT INTO snacks VALUES(3, "POPCORN", 400,"LARGE")')
    cursor.execute('INSERT INTO snacks VALUES(4, "VEG BURGER", 100,"2")')
    cursor.execute('INSERT INTO snacks VALUES(5, "VEG HOT DOG", 80,"2")')
    cursor.execute('INSERT INTO snacks VALUES(6, "GRILLED SANDWICH", 40,"1")')
    cursor.execute('INSERT INTO snacks VALUES(7, "FRENCH FRIES", 40,"MEDIUM")')
    cursor.execute('INSERT INTO snacks VALUES(8, "NACHOS", 150,"-")')
    cursor.execute('INSERT INTO snacks VALUES(9, "CHEESE FRIES", 100,"LARGE ")')
    cursor.execute('INSERT INTO snacks VALUES(10, "MOZZARELLA STICKS", 80,"10")')
    cursor.execute('INSERT INTO snacks VALUES(11, "COFFEE", 80,"100 ML")')
    cursor.execute('INSERT INTO snacks VALUES(12, "CAPPUCCINO", 160,"100 ML")')
    cursor.execute('INSERT INTO snacks VALUES(13, "COOKIES", 50,"5")')
    cursor.execute('INSERT INTO snacks VALUES(14, "CHOCOLATE", 200,"-")')    
    cursor.execute("INSERT INTO snacks VALUES(15, 'PEPSI', 100,'200 ML')")
    cursor.execute("INSERT INTO snacks VALUES(16, 'CHEESE', 20,'5 TBSP')")
    cursor.execute("INSERT INTO snacks VALUES(17, 'VEG MAYONNAISE', 20,'5 TBSP')")
    cursor.execute("INSERT INTO snacks VALUES(18, 'BISLERI', 20,'1 BOTTLE')")
    cursor.execute("INSERT INTO snacks VALUES(19, 'COUPLES COMBO', 500,'1 LARGE DRINK & 1 LARGE POPCORN')")
    cursor.execute("INSERT INTO snacks VALUES(20, 'COMBO #1', 300,'2 MEDIUM DRINKS & 1 MEDIUM POPCORN')")
    cursor.execute("INSERT INTO snacks VALUES(21, 'COMBO #2', 400,'1 MEDIUM DRINK, 1 LARGE DRINK & 1 LARGE POPCORN')")
    cursor.execute("INSERT INTO snacks VALUES(22, 'COMBO #3', 400,'1 LARGE DRINK & LARGE NACHOS')")
    cursor.execute("INSERT INTO snacks VALUES(23, 'KIDS COMBO', 600,'SMALL PEPSI,KIDS TRAY WITH POPCORN, FRUIT SNACKS & MEDIUM BURGER')")
    cursor.execute("INSERT INTO snacks VALUES(24, 'MAHARAJA COMBO', 1000,'2 LARGE POPCORNS, 2 BURGERS, 2 MEDIUM DRINKS, UNLIMITED NACHOS')")
    cursor.execute('select * from snacks')
    record=cursor.fetchall()
    for i in record:
        listprint(i)
        print()
    print('------------------------------------------')
    print('WOULD YOU LIKE TO HAVE SOME SNACKS??')
    print('1. YES')
    print('2. NO')
    list=[]
    choice=input('MAKE CHOICE(1-2): ')
    while choice=='1':
        print()
        pid=input('ENTER PID(1-10): ')
        if pid in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']:
            pid=int(pid)
            quantity=int(input('ENTER QUANTITY: '))
            print('SUCCESS....')
            print()
            cursor.execute('select product, price from snacks where pid=%s',(pid,))
            myresult = cursor.fetchall()
            list.append([myresult[0][0],quantity,myresult[0][1]])        
            print('WOULD YOU LIKE TO HAVE SOME MORE SNACKS??')
            print('1. YES')
            print('2. NO')
            choice=input('MAKE CHOICE(1-2): ')       
        else:
            print('INVALID INPUT GIVEN....')
            print('TRY AGAIN....')
            print()
    else:
        cursor.execute('drop database snacks')
        mc.commit()
        return list
    



