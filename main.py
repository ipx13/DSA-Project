import csv
import random


wishlist = []
owned = []
etc = []
randoms = []
alt_links = []
f_printthis = []

with open('index.csv', 'r', encoding='UTF8') as index_csv:
    csv_reader = csv.reader(index_csv)

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
                query = int(input('how many random albums would you like? '))
                if query <= 0:
                    print('bruh wat\n')
                    continue
                else:
                    break
        except:
            print('enter an integer pls')
        else:
            index = query
            c_index = 0
            while c_index != index:
                randoms.append(random.choice(wishlist))
                c_index += 1

            repl = [(' ', '%20'),
                    (',', '%2C'),
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
                                   'https://rateyourmusic.com/search?searchterm=' + alt_links[count] + '&searchtype=')
                count += 1

            for x in f_printthis:
                print(x)
            break

print('wish:', len(wishlist), '\n'
      'owned:', len(owned), '\n'
      'etc:', len(etc), '\n'
      'total:', len(wishlist + owned + etc))
