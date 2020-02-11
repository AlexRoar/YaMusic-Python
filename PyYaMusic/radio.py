#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#
import json
from PyYaMusic.track import Track
import subprocess
import requests
import time


# Queue work not good
# TODO: make normal query
class Radio:
    def __init__(self, login='', raw_edit=''):
        self.now = ()
        self.next = ()
        self.tracks = []
        self.login = login
        self.raw_edit = raw_edit

    def getTracks(self, que=''):
        cookies = {
            'mda': '0',
            '_ym_isad': '2',
            'Session_id': '3:1556406891.5.0.1556406891904:r0r_vA:12.1|227207001.0.2.0:3|198398.402244.BOys4fFX_wLTsjlfrtZiiYujCdA',
            'sessionid2': '3:1556406891.5.0.1556406891904:r0r_vA:12.1|227207001.0.2.0:3|198398.18991.gVUVw4ZUadiPkdSAcfQ4pVEOpbQ',
            'bltsr': '1',
        }

        if self.raw_edit == '':
            cookies = {
                'yandexuid': '8534847021556406878',
                '_ym_wasSynced': '%7B%22time%22%3A1556406880705%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D',
                '_ym_uid': '15564068811045866983',
                '_ym_d': '1556406881',
                'mda': '0',
                '_ym_isad': '2',
                'Session_id': '3:1556406891.5.0.1556406891904:r0r_vA:12.1|227207001.0.2.0:3|198398.402244.BOys4fFX_wLTsjlfrtZiiYujCdA',
                'sessionid2': '3:1556406891.5.0.1556406891904:r0r_vA:12.1|227207001.0.2.0:3|198398.18991.gVUVw4ZUadiPkdSAcfQ4pVEOpbQ',
                'ys': 'diskchrome.8-22-3#udn.czoxNjQ3MDUwNjp2azrQodCw0YjQsCDQlNGA0LXQvNC%2B0LI%3D',
                'L': 'fw0HcUtKAHNnX1RaV1xCe3hIRGcIQF9vBSQNAhYaXXJAe2E=.1556406891.13848.335772.c1d5d2dc58970caea216848bcffa23a6',
                'yandex_login': self.login,
                'i': 'jxREviG0SFaGqCQxJutJW+cCGxVqlrxtP1FJ3sO5LzxF3BxT7wuW6ZErMIxUNPEAHyUnzPoL6oidaJxjTCiJgAoL5uM=',
                'device_id': 'ac27f1b47303e5935c639c2e6c7c54406659058e0',
                'bltsr': '1',
                'yp': '1871766880.yrtsi.1556406880#1556636423.gpauto.55_876396799999995%3A37_5777814%3A37%3A3%3A1556463623#1871766891.udn.czoxNjQ3MDUwNjp2azrQodCw0YjQsCDQlNGA0LXQvNC%2B0LI%3D',
            }
            headers = {
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                'X-Current-UID': '227207001',
                'Accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
                'Referer': 'https://radio.yandex.ru/user/' + self.login,
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
            }
        else:
            headers = {
                'Accept-Encoding': 'gzip, deflate, br',
                'X-Retpath-Y': 'https%3A%2F%2Fradio.yandex.ru%2Fgenre%2Fpop',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                'X-Current-UID': '227207001',
                'Accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
                'Referer': 'https://radio.yandex.ru/genre/pop',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
            }

        params = (
            ('queue', que),
            ('external-domain', 'radio.yandex.ru'),
            ('overembed', 'no'),
            ('__t', str(time.time() * 1000)[:13])
        )

        if self.raw_edit == '':
            response = requests.get('https://radio.yandex.ru/api/v2.1/handlers/radio/user/' + self.login + '/tracks',
                                    headers=headers, params=params, cookies=cookies)
        else:
            response = requests.get('https://radio.yandex.ru/api/v2.1/handlers/radio/' + self.raw_edit + '/tracks',
                                    headers=headers, params=params, cookies=cookies)

        data = json.loads(response.text)
        print('Gathering list: ')
        n = 1
        for i in data['tracks']:
            track_id = i['track']['id']
            album_id = i['track']['albums'][0]['id']
            title = i['track']['title']
            print('\t'+str(n)+'. '+title+' ('+i['track']['artists'][0]['name']+') ')
            n+=1
            self.tracks.append((track_id, album_id))

        return self.tracks

    def updateTracks(self):
        fl = True
        if (len(self.tracks) == 0):
            self.getTracks()
            self.now = self.tracks.pop(0)
            self.next = self.tracks.pop(0)
        if (len(self.now) == 0):
            fl = False
        if (fl):
            self.tracks = []
            que = str(self.now[0]) + ':' + str(self.now[1]) + ',' + str(self.next[0]) + ':' + str(
                self.next[1])
        else:
            que = ''
        self.getTracks(que=que)

    def start(self):
        self.updateTracks()
        self.now = self.tracks.pop(0)
        self.next = self.tracks.pop(0)
        t = Track()
        t.playByids(self.now[0], self.now[1])
        self.start()

    def radioDaemon(self):
        self.pr = subprocess.Popen(['python3.7', 'radioDaemon.py'])

    def stopDaemon(self):
        self.pr.kill()

    def nextTrack(self):
        self.updateTracks()
        self.now = self.tracks.pop(0)
        self.next = self.tracks.pop(0)

