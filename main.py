import csv
import random

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





print('\nRateYourMusic Database Tool\n'
      '---------------------------')
print('This script requires importing the exported .csv file RYM as "index.csv"')


while True:
    print('\nMain Menu\n'
          '---------\n'
          '[1] Randomize your Wishlist\n'
          '[2] Search the Database\n'
          '[3] Exit')
    try:
        menu_choice = int(input('What would you like to look for? '))
        if menu_choice not in (1, 2, 3):
            print('Please enter an integer between 1-3!\n')
            continue
    except:
        print('Please enter an integer.')
    else:
        if menu_choice == 1:
            with open('index.csv', 'r', encoding='UTF8') as index_csv:
                csv_reader = csv.reader(index_csv)
                for line in csv_reader:
                    if line[8] == 'w':
                        wishlist.append(line)
                    elif line[8] == 'o':
                        owned.append(line)
                    else:
                        etc.append(line)
                print('\n1 | Randomize Your Wishlist!\n'
                      '----------------------------')
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
                                ("'", "%27")]

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
                            f_printthis.append('\n' + cond + ' - ' + fprint[5] + '\n' +
                                               'https://rateyourmusic.com/search?searchterm=' + alt_links[
                                                   count] + '&searchtype=')
                            count += 1

                        for x in f_printthis:
                            print(x)
                        break
        elif menu_choice == 2:
            with open('index.csv', 'r', encoding='UTF8') as index_csv:
                csv_reader = csv.reader(index_csv)
                while True:
                    print('\n2 | Search the Database!\n'
                          '------------------------')
                    print('[1] Artist/s Name\n'
                          '[2] Album Name\n'
                          '[3] Year Released\n'
                          '[4] Return')
                    try:
                        search_choice = int(input('What would you like to look for? '))
                        if search_choice not in (1, 2, 3, 4):
                            print('Please enter an integer between 1-4!\n')
                            continue
                    except:
                        print('Please enter an integer.')
                    else:
                        csv_reader = csv.reader(index_csv)
                        for line in csv_reader:
                            albums.append(line[5])
                            years.append(line[6])
                            if line[1] != '':
                                artists.append(line[1] + ' ' + line[2])
                            else:
                                artists.append(line[2])

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
                            print('\nDisplaying all results for the artist/s >>> ' + search_art + ' <<<')
                            print('---------------------------------------------------------------')
                            if len(indexes) != 0:
                                for index in indexes:
                                    print(artists[index] + ' - ' + albums[index] + ' (' + years[index] + ')')
                            else:
                                print('No match found :( Try checking your spelling or capitalization.')
                            print('---------------------------------------------------------------')
                            indexes.clear()

                        elif search_choice == 2:
                            search_alb = input('\nEnter the Album Name: ')
                            id = 0
                            for line in albums:
                                if line == search_alb:
                                    indexes.append(id)
                                id += 1
                            print('\nDisplaying all results for the album >>> ' + search_alb + ' <<<')
                            print('---------------------------------------------------------------')
                            if len(indexes) != 0:
                                for index in indexes:
                                    print(artists[index] + ' - ' + albums[index] + ' (' + years[index] + ')')
                            else:
                                print('No match found :( Try checking your spelling or capitalization.')
                            print('---------------------------------------------------------------')
                            indexes.clear()

                        elif search_choice == 3:
                            search_yr = input('\nEnter the Release Year: ')
                            id = 0
                            for line in years:
                                if line == search_yr:
                                    indexes.append(id)
                                id += 1

                            print('\nDisplaying all results for the release year >>> ' + search_yr + ' <<<')
                            print('---------------------------------------------------------------')
                            if len(indexes) != 0:
                                for index in indexes:
                                    print(artists[index] + ' - ' + albums[index] + ' (' + years[index] + ')')
                            else:
                                print('No match found :( Try checking your spelling or capitalization.')
                            print('---------------------------------------------------------------')
                            indexes.clear()

                        elif search_choice == 4:
                            break
                        break
        elif menu_choice == 3:
            print('------------------------------\n'
                  'Thanks for using this program!')
            break


