
bb = []
while True:
    global shop
    shop = input("Do you want to add or take away from your shopping list. Say A for add or D for take away. Type Can I see my list if you want to see your list:")
    if shop == 'A' or shop == 'a':
        no = input('What do you want to add:')
        if bb.count(no) == 0:
            bb.append(no)
            
        else:
            print('You cant add more than once')
           
    global what
    if shop == 'D' or shop == 'd':
        what = input('What do you want to take away:')
        if bb.count(what) == 0:
            print("You cant remove that because it is not in your list")
        else:
            bb.remove(what)
            
                
    if shop == 'Can I see my list' or shop == 'can I see my list':
        for i in bb:
            print(i)