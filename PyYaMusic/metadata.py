#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#

import json
import random
from PyYaMusic.track import Track
import requests
import os.path
import urllib.parse
from mutagen.easyid3 import EasyID3
from tqdm import tqdm


class Metadata:
    path = ''

    def __init__(self, path=''):
        if len(path) != 0:
            if path[-1] != '':
                path += '/'
        self.path = path

    def allMetaDataInDir(self, recursively=True, prompt=True, printData=False):
        path = self.path
        if len(path) != 0:
            if path[-1] == '/':
                self.path = path[:-1]
        with os.scandir(self.path) as path:
            print('\nProcessing ' + self.path)
            path = list(path)
            for file in tqdm(range(len(path))):
                file = path[file]
                if file.is_dir(follow_symlinks=False) and recursively:
                    m = Metadata(file.path)
                    m.allMetaDataInDir(recursively, prompt, printData)
                elif file.is_dir(follow_symlinks=False):
                    continue
                filename, file_extension = os.path.splitext(file.path)
                if (file_extension == '.mp3'):
                    try:
                        self.fileMetadata(file.path, prompt, printData)
                    except:
                        print('GlobalError with ' + file.path)

    def fileMetadata(self, file=float('nan'), prompt=False, printData=False):
        if file == float('nan'):
            file = self.path

        bn = os.path.basename(file)
        rp = os.path.relpath(file)

        name = urllib.parse.unquote(bn)
        name = name.replace('_', ' ')
        name = ''.join(name.split('.')[:-1])

        try:
            audio = EasyID3(file)
            name += ' ' + audio['artist'][0]
        except:
            pass

        tr = Track('/'.join(os.path.abspath(file).split('/')[:-1]))
        res = tr.search(name)
        if (res == []):
            try:
                name = ''
                audio = EasyID3(file)
                name += audio['title'] + ' ' + audio['artist'][0]
                res = tr.search(name)
                if (res != []):
                    print('Fixed. Found')
            except:
                pass

        if res != []:
            if printData:
                inf = tr.getTrackInfo(res[0][0], res[0][1])
                print('Old: ' + name, '<=> new: ' + inf['artists'][0]['name'] + ' ' + inf['track']['title'])
            if prompt:
                i = input('Y/n ?: ')
                if (i != 'Y'):
                    return
            tr.metadataForFirst(file)
