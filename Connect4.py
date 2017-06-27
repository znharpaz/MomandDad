a = int(input('Pick a column.'))
aa=[[],[],[],[],[],[]]
for i in aa:
    for x in range(0,7):
        i.append('-')
print(aa)
for r in range(0,6):
    print() 
    for c in range(0,7):
        print(aa[r][c],end = '')
while True:
    for a in range(5,0,-1):
        if a == '-':
            c =+ 1
        else:
            aa[r][c] = 'x'
    
           

       
        
    
    

    
        