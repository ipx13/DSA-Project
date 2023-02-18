import csv
import random

def randomize():
    for line in csv_reader:
        if line[8] == 'w':
            wishlist.append(line)
        elif line[8] == 'o':
            owned.append(line)
        else:
            etc.append(line)

    while True:
        try:
            while True:
                query = int(input('How many results would you like to generate? '))
                if query <= 0:
                    print('Please enter a nonzero positive integer.\n')
                    continue
                else:
                    break
        except:
            print('Please enter an integer.\n')
        else:
            index = query
            c_index = 0
            while c_index != index:
                randoms.append(random.choice(wishlist))
                c_index += 1

            repl = [(' ', '%20'),
                    (',', '%2C'),
                    ('&#092;', '/'),
                    ('&#34;', '"'),
                    ('&amp;', '%26'),
                    (';', '%3B'),
                    (':', '%3A'),
                    ('/', '%2F'),
                    ('+', '%2B'),
                    ("'","%27")]

            for r_albums in randoms:
                cu_album = r_albums[5]
                if r_albums[1] != str(''):
                    ifcond1 = r_albums[1] + ' ' + r_albums[2]
                    alt_links.append(ifcond1 + ' - ' + cu_album)

                    counter = 0
                    for altx in alt_links:
                        for x, y in repl:
                            alt_links[counter] = alt_links[counter].replace(x, y)
                        counter += 1

                elif r_albums[2] != str(''):
                    ifcond2 = r_albums[2]
                    alt_links.append(ifcond2 + ' - ' + cu_album)

                    counter = 0
                    for altx in alt_links:
                        for x, y in repl:
                            alt_links[counter] = alt_links[counter].replace(x, y)
                        counter += 1

            count = 0
            for fprint in randoms:
                if fprint[1] != str(''):
                    cond = fprint[1] + ' ' + fprint[2]
                elif fprint[2] != str(''):
                    cond = fprint[2]
                f_printthis.append(cond + ' - ' + fprint[5] + '\n' +
                                   'https://rateyourmusic.com/search?searchterm=' + alt_links[count] + '&searchtype=\n')
                count += 1

            for x in f_printthis:
                print(x)
            break

def search():
    while True:
        print('\nSearch the database!\n'
              '[1] Artist/s Name\n'
              '[2] Album Name\n'
              '[3] Year Released\n'
              '[4] Return')
        try:
            search_choice = int(input('What would you like to look for? '))
            if search_choice not in (1, 2, 3, 4):
                print('Please enter an integer between 1-4!\n')
                continue
        except:
            print('Please enter an integer.\n')
        else:
            for line in csv_reader:
                albums.append(line[5])
                years.append(line[6])
                if line[1] != '':
                    artists.append(line[1] + ' ' + line[2])
                else:
                    artists.append(line[2])
            artists.pop(0)
            albums.pop(0)
            years.pop(0)

            repl = [('&#34;', '"'),
                    ('&#092;', '/'),
                    ('&amp;', '&')]
            c1 = 0
            c2 = 0
            c3 = 0
            for i in artists:
                for x, y in repl:
                    artists[c1] = artists[c1].replace(x, y)
                c1 += 1
            for j in albums:
                for x, y in repl:
                    albums[c2] = albums[c2].replace(x, y)
                c2 += 1
            for k in albums:
                for x, y in repl:
                    albums[c3] = albums[c3].replace(x, y)
                c3 += 1

            if search_choice == 1:
                search_art = input('\nEnter the Artist Name: ')
                id = 0
                for line in artists:
                    if line == search_art:
                        indexes.append(id)
                    id += 1
                print('\nDisplaying all results for "', search_art + '":\n--------------------------------------')
                for index in indexes:
                    print(artists[index] + ' - ' + albums[index] + ' (' + years[index] + ')')

            elif search_choice == 2:
                search_art = input('Enter the Artist Name: ')
            elif search_choice == 3:
                search_art = input('Enter the Artist Name: ')
            elif search_choice == 4:
                search_art = input('Enter the Artist Name: ')
            break

def menu():
    print('\nMenu\n'
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
                randomize()
            elif menu_choice == 2:
                search()
            elif menu_choice == 3:
                print('hehe')
            elif menu_choice == 4:
                print('bye')
            break

# Data Structures for the Randomizer Function
wishlist = []
owned = []
etc = []
randoms = []
alt_links = []
f_printthis = []

# Data Structures for the Search Function
artists = []
albums = []
years = []
indexes = []

with open('index.csv', 'r', encoding='UTF8') as index_csv:
    csv_reader = csv.reader(index_csv)

    print('welcome to mi programme!')
    while True:
        menu()
        while True:
            try:
                print('\nWhere would you like to go?\n'
                      '[1] Menu\n'
                      '[2] Exit the program\n')
                returnq = int(input('I would like to: '))
                if returnq in (1, 2):
                    if returnq == 1:
                        menu()
                    elif returnq == 2:
                        print('Thanks for using this program!')
                        break
                    else:
                        print('Please enter only either 1 or 2!')
                        continue
            except:
                print('Please only enter integers! Either 1 or 2 will do :)')
                continue
            break
        break





print('wish:', len(wishlist), '\n'
      'owned:', len(owned), '\n'
      'etc:', len(etc), '\n'
      'total:', len(wishlist + owned + etc))
