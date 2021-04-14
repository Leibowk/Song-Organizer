import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError

def main():
    basepath = '/Users/kyle/Music/'
    #Want to get it working on a phone 
    # basepath = 'This PC\moto g(7) power\Internal shared storage\Music'

    for dirpath, dirnames, files in os.walk(basepath):
        for aSong in files:
            if aSong != "desktop.ini":
                song = dirpath + '/' + aSong
                # print(song)
                changeArtist(song)

def changeArtist(song):
    try: 
        audio = ID3(song)
    except ID3NoHeaderError:
        print("Adding ID3 header")
        audio = ID3()
    
    stringPath = song.__str__()
    trash = stringPath.split('/')
    artistName = trash[5].split('-')[0]
    
    track = EasyID3(song)
    track["artist"] = artistName
    track.save(v2_version=3)


if __name__ == "__main__":
    main()