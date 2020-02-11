#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#

import json
import random
from PyYaMusic import obfuscYandex
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error, USLT, TCON, TDRC
from mutagen.easyid3 import EasyID3
import os, urllib.parse
from pydub import AudioSegment
from pydub.playback import play
import requests


class Track:
    def __init__(self, default_path='cache/'):
        if len(default_path) != 0:
            if default_path[-1] != '':
                default_path += '/'

        if not os.path.isdir(default_path):
            os.makedirs(default_path)

        self.default_path = default_path
        self.tracks = []  # Tuples (track id, album id)
        self.headers = {
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Current-UID': '227207001',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive'
        }

    def search(self, text):
        self.tracks = []

        params = (
            ('text', text),
            ('type', 'tracks'),
            ('ncrnd', '0.22174742529705926'),
            ('lang', 'ru'),
            ('external-domain', 'music.yandex.ru'),
            ('overembed', 'false'),
        )

        response = requests.get('https://music.yandex.ru/handlers/music-search.jsx', headers=self.headers,
                                params=params,
                                cookies={})
        data = response.json()['tracks']['items']
        for i in data:
            self.tracks.append((i['id'], i['albums'][0]['id']))
        if self.tracks == []:
            print('Not found warning: ' + text)
        return self.tracks

    def load_data(self, track_id, album_id):
        params_inf = (
            ('track', str(str(track_id) + ':' + str(album_id))),
            ('lang', 'ru'),
            ('external-domain', 'music.yandex.ru'),
            ('overembed', 'false'),
            ('ncrnd', '0.13835443477395826'),
        )

        info = requests.get('https://music.yandex.ru/handlers/track.jsx', headers=self.headers, params=params_inf,
                            cookies={})
        info = json.loads(info.text)
        return info

    def load_data_tuple(self, trackalbum):
        return self.load_data(trackalbum[0], trackalbum[1])

    def download(self, track_id, album_id, name='auto', rewrite=False):
        track_id = str(track_id)
        album_id = str(album_id)
        link = self.getDownloadLink(track_id, album_id)

        response = requests.get(link[0], headers=self.headers, params=link[1])

        name = urllib.parse.quote(name, safe='')
        if (name == 'auto'):
            info = self.load_data(track_id, album_id)
            name = info['artists'][0]['name'] + '_' + info['track']['title'] + str(track_id) + '.mp3'
        else:
            if name.split('.')[-1] != 'mp3':
                name = name + '.mp3'

        # print(name)
        name = name.replace(' ', '_')
        name = urllib.parse.quote(name, safe='')
        if (os.path.isfile(self.default_path + name) and not rewrite):
            print('\nPending... ' + name)
            return 201
        name = self.default_path + name
        audio = open(name, 'wb')
        audio.write(response.content)
        audio.close()

        info = self.getTrackInfo(track_id, album_id)
        # print('https://' + (info['track']['coverUri'][:-2]) + 'm1000x1000')

        headers = {
            'Referer': 'https://music.yandex.ru/album/' + album_id + '/track/' + track_id,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        }

        response = requests.get('https://' + (info['track']['coverUri'][:-2]) + 'm1000x1000',
                                headers=headers)

        audio = MP3(name, ID3=ID3)
        try:
            audio.add_tags()
        except error:
            pass

        audio.tags.add(
            APIC(
                encoding=3,  # 3 is for utf-8
                mime='image/png',  # image/jpeg or image/png
                type=3,  # 3 is for the cover image
                desc=u'Cover',
                data=response.content
            )
        )
        try:
            if (info['track']['lyricsAvailable'] and len(info['lyric']) != 0):
                audio.tags.add(USLT(encoding=3, lang=u'eng', desc=u'desc', text=info['lyric'][0]['fullLyrics']))
        except:
            pass

        try:
            audio.tags.add(TCON(encoding=3, text=u'' + str(info['track']['albums'][0]['genre'])))
        except:
            pass
        try:
            audio.tags.add(TDRC(encoding=3, text=u'' + str(info['track']['albums'][0]['year'])))
        except:
            pass
        audio.save()
        audio = EasyID3(name)
        audio['title'] = info['track']['title']
        audio['artist'] = info['track']['artists'][0]['name']
        audio['album'] = info['track']['albums'][0]['title']
        audio['composer'] = u""  # clear

        audio.save()

        # print(json.dumps(info))

        return response.status_code

    def downloadFirst(self, name='auto'):
        if (len(self.tracks) == 0):
            raise Exception('No tracks found')
        else:
            self.download(self.tracks[0][0], self.tracks[0][1], name=name)

    def metadataForFirst(self, path):
        if (len(self.tracks) == 0):
            raise Exception('No tracks found')
        else:
            track_id = self.tracks[0][0]
            album_id = self.tracks[0][1]
            track_id = str(track_id)
            album_id = str(album_id)
            info = self.getTrackInfo(track_id, album_id)

            headers = {
                'Referer': 'https://music.yandex.ru/album/' + album_id + '/track/' + track_id,
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
            }

            try:
                audio = MP3(path, ID3=ID3)
                audio.delete()
                try:
                    audio.add_tags()
                except error:
                    pass
                try:
                    response = requests.get('https://' + (info['track']['coverUri'][:-2]) + 'm1000x1000',
                                            headers=headers)
                    audio.tags.add(
                        APIC(
                            encoding=3,  # 3 is for utf-8
                            mime='image/png',  # image/jpeg or image/png
                            type=3,  # 3 is for the cover image
                            desc=u'Cover',
                            data=response.content
                        )
                    )
                except:
                    print('Cover error: ' + path)
                if (info['track']['lyricsAvailable']):
                    audio.tags.add(USLT(encoding=3, lang=u'eng', desc=u'desc', text=info['lyric'][0]['fullLyrics']))

                audio.tags.add(TCON(encoding=3, text=u'' + str(info['track']['albums'][0]['genre'])))
                audio.tags.add(TDRC(encoding=3, text=u'' + str(info['track']['albums'][0]['year'])))
                audio.save()
            except:
                print('Error occurred with metadata for ' + path)

            try:
                audio = EasyID3(path)
                audio['title'] = info['track']['title']
                audio['artist'] = info['track']['artists'][0]['name']
                audio['album'] = info['track']['albums'][0]['title']
                audio['composer'] = u""  # clear
                audio.save()
            except:
                print('Error occurred with metadata for ' + path)

    def getDownloadLink(self, track_id, album_id):
        track_id = str(track_id)
        album_id = str(album_id)
        __t = str(random.randint(1500000000000, 10000000000000))
        headers = {
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Retpath-Y': 'https%3A%2F%2Fmusic.yandex.ru%2Falbum%2F1672742%2Ftrack%2F10294529',
            'X-Current-UID': '227207001',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://music.yandex.ru/album/' + track_id + '/track/' + album_id,
        }

        params = (
            ('hq', '1'),
            ('strm', '0'),
            ('external-domain', 'music.yandex.ru'),
            ('overembed', 'no'),
            ('__t', __t),
        )

        response = requests.get(
            'https://music.yandex.ru/api/v2.1/handlers/track/' + track_id + ':' + album_id + '/web-album_track-track-track-fridge/download/m',
            headers=headers, params=params, cookies={})
        try:
            result = json.loads(response.text)
            src = result['src']
        except:
            print('Undone: ' + track_id + ' ' + album_id)

        params = (
            ('sign', '9ba9f320a83d37549d4f3ba69dd8386f416aa3f63a51e7579f0d85b95736f6a9'),
            ('ts', '5c310e84'),
            ('format', 'json'),
            ('external-domain', 'music.yandex.ru'),
            ('overembed', 'no'),
            ('__t', __t),
        )

        headers = {
            'Origin': 'https://music.yandex.ru',
            'Accept-Encoding': 'identity;q=1, *;q=0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Range': 'bytes=0-',
            'chrome-proxy': 'frfr',
        }

        response = requests.get(src, headers=headers, params=params)

        result = json.loads(response.text)
        params = (
            ('track-id', track_id),
            ('play', 'false'),
        )

        path_end = 'https://' + result['host'] + '/get-mp3/' + obfuscYandex.obfuscateYandex(
            result['path'][1:] + result['s']) + '/' + result['ts'] + result['path']
        return (path_end, params)

    def getFirstDownloadLink(self):
        if (len(self.tracks) == 0):
            raise Exception('No tracks found')
        else:
            return self.getDownloadLink(self.tracks[0][0], self.tracks[0][1])

    def generateLinkWithParams(self, link, params):
        if (len(params) != 0):
            link += '?'
        for i in params:
            link += i[0] + '=' + i[1] + '&'
        link = link[:-1]
        return link

    def playFirst(self):
        if (len(self.tracks) == 0):
            raise Exception('No tracks found')
        link = self.getFirstDownloadLink()
        link = self.generateLinkWithParams(link[0], link[1])
        self.downloadFirst('cache')
        self.playMusic(self.default_path + 'cache.mp3')

    def playByids(self, track_id, album_id):
        link = self.getDownloadLink(track_id, album_id)
        link = self.generateLinkWithParams(link[0], link[1])
        p = self.default_path
        if not os.path.exists("cache/"):
            os.mkdir('cache/')
        self.default_path = 'cache/'
        self.download(track_id, album_id, 'cache', True)
        self.default_path = p
        self.playMusic('cache/cache.mp3')

    def getTrackInfo(self, track_id, album_id):
        cookies = {}

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Retpath-Y': 'https://music.yandex.ru/album/' + str(album_id) + '/track/' + str(track_id),
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
            'X-Current-UID': '227207001',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://music.yandex.ru/album/' + str(album_id) + '/track/' + str(track_id),
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        }

        params = (
            ('track', str(track_id) + ':' + str(album_id)),
            ('lang', 'en'),
            ('external-domain', 'music.yandex.ru'),
            ('overembed', 'false'),
            ('ncrnd', '0.33253286876165544'),
        )

        response = requests.get('https://music.yandex.ru/handlers/track.jsx', headers=headers, params=params,
                                cookies=cookies)

        return json.loads(response.text)

    def playMusic(self, path):
        song = AudioSegment.from_mp3(path)
        play(song)
