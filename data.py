#Album dictionary
ALBUMS = {}
#File path
FILE = "Pink_Floyd_DB.txt"
lastAddedAlbum = ""
lastAddedSong = ""
def createDataBase():
    file = open(FILE, 'r')
    #run on the entire file
    for line in file:
      #Album name lines start with "#"
      if('#' in line):
          lastAddedAlbum = line[1:line.index(':')]
          #add to the albums dictionary a new entry where:
          # Key: Album Name | Value: Tuple of (Song infos (empty for now),release date)
          ALBUMS.update({lastAddedAlbum: ({},line[line.index("::")+2:])})
      #Song name lines start with "*"
      elif('*' in line):
          #split the song data between each "::"
          songData = line.split("::")
          lastAddedSong = songData[0][1:]
          #add to the empty dictionary in each album key entries as such:
          #Key = Song name Values: 1.Song writer 2.Length 3.String of all lyrics
          ALBUMS[lastAddedAlbum][0].update({songData[0][1:]:[
              songData[1],
              songData[2],
              songData[3],
          ]})
      else:
          #if not new song or album concat lyric to previous song lyrics
          #Albums[lastAddedAlbum][0] is the dictionary of songs and [1] is release date
          ALBUMS[lastAddedAlbum][0][lastAddedSong][2]+=line
    file.close()

#return album dictionary
def getAlbums():
    return ALBUMS
#return song data
def getSongData(SongName):
    #iterate over every album
    for Album in ALBUMS:
        #if song is in current album
        if(SongName in ALBUMS[Album][0]):
            #return its data
            return (Album,ALBUMS[Album][0][SongName])

#get song titles from word included
def getSongsFromWord(Word):
    #song title arrays
    songs = []
    for Album in ALBUMS:
        #for every song in album
        for Song in ALBUMS[Album][0]:
            #if the title contains the word (lower for case insensitivity)
            if Word.lower() in Song.lower():
                #add song to list
                songs.append((Song))
    return songs

#get songs that include given lyric
def getSongsFromLyric(Lyric):
    songs = []
    for Album in ALBUMS:
        #for every song in album
        for Song in ALBUMS[Album][0]:
            #if given song lyric contains the given lyrics
            if Lyric.lower() in ALBUMS[Album][0][Song][2].lower():
                songs.append((Song))
    return songs