aa=[[],[],[],[],[],[]]
for i in aa:
    for x in range(0,7):
        i.append('-')
        

        
while True:
    a = int(input('Player one pick a column.'))
    for i in range(5,-1,-1):
        if aa[i][a] == '-':
            aa[i][a] = 'x'
            break
        elif aa[i][a] == 'x':
            pass
        if aa[0][a] != '-':
            i = 5
            a = int(input('Player one pick a column.'))
            
        
    for r in range(0,6):
        print() 
        for c in range(0,7):
            print(aa[r][c],end = '')
    
    for i in range(0,3):
        for h in range(0,7):
            if aa[i][h] == 'x' and aa[i+1][h] == 'x' and aa[i+2][h] == 'x' and aa[i+3][h] == 'x':
                print('You Win!')
    
    for i in range(0,4):
        for h in range(0,6):
            if aa[i][h] == 'x' and aa[i][h+1] == 'x' and aa[i][h+2] == 'x' and aa[i][h+3] == 'x' and aa[i][h+4] == 'x':
                print('You Win!')
    
                
    for i in range(0,2):
        for h in range(0,3):
            if aa[i][h] == 'x' and aa[i+1][h+1] == 'x' and aa[i+2][h+2] == 'x' and aa[i+3][h+3] == 'x':
                print('You Win!')
                break
    
    
    
    a = int(input('Player two pick a column.'))
    for i in range(5,-1,-1):
        if aa[i][a] == '-':
            aa[i][a] = 'o'
            break
        elif aa[i][a] == 'o':
            pass
        if aa[0][a] != '-':
            i = 5
            a = int(input('Player two pick a column.'))
    for r in range(0,6):
        print() 
        for c in range(0,7):
            print(aa[r][c],end = '')
            
            
    for i in range(0,3):
        for h in range(0,7):
            if aa[i][h] == 'o' and aa[i+1][h] == 'o' and aa[i+2][h] == 'o' and aa[i+3][h] == 'o':
                print('You Win!')
                break
            
            
    for i in range(0,4):
        for h in range(0,6):
            if aa[i][h] == 'o' and aa[i][h+1] == 'o' and aa[i][h+2] == 'o' and aa[i][h+3] == 'o' and aa[i][h+4] == 'o':
                print('You Win!')
           
        
   
    
    
    
    
           

       
        
    
    

    
        