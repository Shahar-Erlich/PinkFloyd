ALBUMS = {}
FILE = "Pink_Floyd_DB.txt"
lastAdded = ""
def createDataBase():
    file = open(FILE, 'r')
    for line in file:
      if('#' in line):
          lastAdded = line[1:line.index(':')]
          ALBUMS.update({lastAdded: ({},line[line.index("::")+2:])})
      if('*' in line):
          ALBUMS[lastAdded][0].update({line[1:line.index(':')]:[]})
    for album in ALBUMS:
        print(album)
        print(ALBUMS[album])