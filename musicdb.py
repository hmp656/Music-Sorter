import os, re, time, json
from mutagen.easyid3 import EasyID3 as easyID


# get all mp3s
def getFiles():
    files = []
    pattern = re.compile(r'\.mp3$')

    for i in os.listdir():
        if pattern.search(i):
            files.append(i)

    return files


# get meta data for one file
def getMetaData(file):
    string = easyID(file)
    audio = r'{} by {}'.format(string['title'][0], string['artist'][0])

    return [audio, string['title'][0], string['artist'][0]]


# rename file
def renameFile(file, name):
    path = os.path.abspath('.')
    os.rename(file, name)
    return path


# create file with all the meta data
def writeDB(dictionary):
    j = json.dumps(dictionary, indent=4)
    with open('muscdb.json', 'w') as f:
        f.write(j)
        f.close()
    return 'Success'


# put it all together
def main():
    files = getFiles()
    metadata = {}

    for file in files:
        mets = getMetaData(file)
        metadata.update({mets[1] : mets[2]})
        name = r'{}.mp3'.format(mets[0])
        try:
            renameFile(file, name)
        except FileExistsError:
            name = r'{}(copy).mp3'.format(mets[0])
            renameFile(file, name)
        except Exception as e:
            return e

    writeDB(metadata)
    pass


if __name__ == '__main__':
    main()

    test = input()
    exit()
