ALBUMS = {}
FILE = "Pink_Floyd_DB.txt"
lastAddedAlbum = ""
lastAddedSong = ""
def createDataBase():
    file = open(FILE, 'r')
    for line in file:
      if('#' in line):
          lastAddedAlbum = line[1:line.index(':')]
          ALBUMS.update({lastAddedAlbum: ({},line[line.index("::")+2:])})
      elif('*' in line):
          songData = line.split("::")
          lastAddedSong = songData[0][1:]
          ALBUMS[lastAddedAlbum][0].update({songData[0][1:]:[
              songData[1],
              songData[2],
              songData[3],
          ]})
      else:
          ALBUMS[lastAddedAlbum][0][lastAddedSong][2]+=line
    # for album in ALBUMS:
    #     print(album)
    #     print(ALBUMS[album])
def getAlbums():
    return ALBUMS
def getSongData(SongName):
    for Album in ALBUMS:
        if(SongName in ALBUMS[Album][0]):
            return (Album,ALBUMS[Album][0][SongName])

def getSongsFromWord(Word):
    songs = []
    for Album in ALBUMS:
        for Song in ALBUMS[Album][0]:
            if Word.lower() in Song.lower():
                songs.append((Song))
    return songs
def getSongsFromLyric(Lyric):
    songs = []
    for Album in ALBUMS:
        for Song in ALBUMS[Album][0]:
            if Lyric.lower() in ALBUMS[Album][0][Song][2].lower():
                songs.append((Song))
    return songs
