#Album dictionary
ALBUMS = {}
#File path
FILE = "Pink_Floyd_DB.txt"
last_added_album = ""
last_added_song = ""
def parse_text_file():
    '''Parses the text file into fitting data structures'''
    with open(FILE, 'r') as file:
        #run on the entire file
        for line in file:
          #Album name lines start with "#"
          if ('#' in line):
              last_added_album = line[1:line.index(':')]
              #add to the albums dictionary a new entry where:
              # Key: Album Name | Value: Tuple of (Song infos (empty for now),release date)
              ALBUMS.update({last_added_album: ({},line[line.index("::")+2:])})
          #Song name lines start with "*"
          elif ('*' in line):
              #split the song data between each "::"
              song_data = line.split("::")
              last_added_song = song_data[0][1:]
              #add to the empty dictionary in each album key entries as such:
              #Key = Song name Values: 1.Song writer 2.Length 3.String of all lyrics
              ALBUMS[last_added_album][0].update({song_data[0][1:]:[
                  song_data[1],
                  song_data[2],
                  song_data[3],
              ]})
          else:
              #if not new song or album concat lyric to previous song lyrics
              #Albums[last_added_album][0] is the dictionary of songs and [1] is release date
              ALBUMS[last_added_album][0][last_added_song][2]+=line



def get_song_data(song_name):
    '''return the data of a song by given name'''
    #iterate over every album
    for Album in ALBUMS:
        #if song is in current album
        if(song_name in ALBUMS[Album][0]):
            #return its data
            return (Album,ALBUMS[Album][0][song_name])


def get_songs_from_word(Word):
    '''get song titles that contain a word given as parameter'''
    #song title arrays
    songs = []
    for Album in ALBUMS:
        #for every song in album
        for Song in ALBUMS[Album][0]:
            #if the title contains the word (lower for case insensitivity)
            if Word.lower() in Song.lower():
                #add song to list
                songs.append(Song)
    return songs

def get_songs_from_lyric(Lyric):
    '''get songs that include given lyric in their lyrics'''
    songs = []
    for Album in ALBUMS:
        #for every song in album
        for Song in ALBUMS[Album][0]:
            #if given song lyric contains the given lyrics
            if Lyric.lower() in ALBUMS[Album][0][Song][2].lower():
                songs.append((Song))
    return songs
