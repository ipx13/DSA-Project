while True:
    print("hey there")

    n = 1
    for n in range(0, n):
        print('\nWhere would you like to go?\n'
              '[1] Menu\n'
              '[2] Exit the program\n')
        returnq = input('I would like to: ')
        if returnq == '1':
            n -= 1
            continue
        elif returnq == '2':
            print('Thanks for using this program!')
            n -= 1
            break
        else:
            print('man whatcha doin')
        print(n)
        break

