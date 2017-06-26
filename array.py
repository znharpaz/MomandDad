
bb = []
while True:
    global shop
    shop = input("Do you want to add or take away from your shopping list. Say A for add or D for take away:")
    if shop == 'A':
        no = input('What do you want to add:')
        if bb.count(no) == 0:
            bb.append(no)
            print(bb)
        else:
            print('You cant add more than once')
            print(bb)
    global what
    if shop == 'D':
        what = input('What do you want to take away:')
        if bb.count(what) == 0:
            print("You cant remove that because it is not in your list")
        else:
            bb.remove(what)
            print(bb)
        
    
    
    

   
  
    
        
         
  
    