aa=[[],[],[],[],[],[]]
for i in aa:
    for x in range(0,7):
        i.append('-')
        

        
while True:
    a = int(input('Pick a column.'))
    aa[5][a] = 'x'
    for i in range(5,0,-1):
        if aa[i][a] == 'x':
            break
        elif aa[i][a] == '-':
            aa[i][a] = 'x'
        
        
    for r in range(0,6):
        print() 
        for c in range(0,7):
            print(aa[r][c],end = '')
    
    
    
    
           

       
        
    
    

    
        