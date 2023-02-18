print('Menu\n'
          '[1] Randomize your Wishlist\n'
          '[2] Search the Database\n'
          '[3] See your RYM Stats\n'
          '[4] Exit')

while True:
    try:
        menu_choice = int(input('What would you like to look for? '))
        if menu_choice not in (1, 2, 3, 4):
            print('Please enter an integer between 1-4!\n')
            continue
    except:
        print('Please enter an integer.\n')
    else:
        if menu_choice == 1:
            print('kek')
        elif menu_choice == 2:
            print('number2')
        elif menu_choice == 3:
            print('hehe')
        elif menu_choice == 4:
            print('bye')
        break