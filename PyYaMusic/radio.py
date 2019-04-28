#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#
import json
import random
from PyYaMusic.track import Track
import subprocess


# Queue work not good
# TODO: make normal query
class Radio:
    def __init__(self, login=''):
        self.now = ()
        self.next = ()
        self.tracks = []
        self.login = login

    def getTracks(self, que=''):
        import requests

        cookies = {}

        headers = {
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Retpath-Y': 'https%3A%2F%2Fradio.yandex.ru%2Fuser%2F' + self.login,
            'X-Current-UID': '227207001',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://radio.yandex.ru/user/' + self.login,
        }

        params = (
            ('queue', que),
            ('external-domain', 'radio.yandex.ru'),
            ('overembed', 'no'),
            ('__t', str(random.randint(1500000000000, 10000000000000))),
        )

        response = requests.get('https://radio.yandex.ru/api/v2.1/handlers/radio/user/' + self.login + '/tracks',
                                headers=headers, params=params, cookies=cookies)

        data = json.loads(response.text)
        for i in data['tracks']:
            track_id = i['track']['id']
            album_id = i['track']['albums'][0]['id']
            self.tracks.append((track_id, album_id))
        return self.tracks

    def updateTracks(self):
        fl = True
        if (len(self.tracks) == 0):
            self.getTracks()
        if (len(self.now) == 0):
            fl = False
        if (fl):
            que = str(self.previous[0]) + ':' + str(self.previous[1]) + ',' + str(self.next[0]) + ':' + str(
                self.next[1])
        else:
            que = ''
        self.getTracks(que=que)

    def start(self):
        if (len(self.tracks) <= 2):
            if (len(self.tracks) == 0):
                self.updateTracks()
                self.now = self.tracks.pop(random.randint(0, len(self.tracks) - 1))
                self.next = self.tracks.pop(random.randint(0, len(self.tracks) - 1))
            else:
                self.updateTracks()
        else:
            if (self.next == ()):
                self.next = self.tracks.pop(random.randint(0, len(self.tracks) - 1))
            track = self.tracks.pop(random.randint(0, len(self.tracks) - 1))
            self.now = self.next
            self.next = track
        t = Track()
        t.playByids(self.now[0], self.now[1])
        self.start()

    def radioDaemon(self):
        self.pr = subprocess.Popen(['python', 'yaMusic/radioDaemon.py'])

    def stopDaemon(self):
        self.pr.kill()

    def next(self):
        self.stopDaemon()
        self.radioDaemon()
