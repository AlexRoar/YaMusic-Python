#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#
import requests
import json
from PyYaMusic.track import Track


class Playlist:
    def __init__(self, id='', owner='music-blog'):
        self.id = id
        self.owner = owner

    def search(self, name):
        pass

    def get_inf(self, id='auto', owner='auto'):
        if (id == 'auto'): id = self.id
        if (owner == 'auto'): owner = self.owner

        cookies = {}

        headers = {
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Retpath-Y': 'https://music.yandex.ru/users/music-blog/playlists/1665',
            'X-Current-UID': '227207001',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://music.yandex.ru/users/music-blog/playlists/1665',
        }

        params = (
            ('owner', owner),
            ('kinds', str(id)),
            ('light', 'true'),
            ('madeFor', ''),
            ('withLikesCount', 'true'),
            ('lang', 'ru'),
            ('external-domain', 'music.yandex.ru'),
            ('overembed', 'false'),
            ('ncrnd', '0.23457215643686902'),
        )

        response = requests.get('https://music.yandex.ru/handlers/playlist.jsx', headers=headers, params=params,
                                cookies=cookies)
        return json.loads(response.text)

    def downloadAll(self, dir='auto'):
        data = self.get_inf()
        if (dir == 'auto'):
            dir = data['playlist']['title']
            import os
            if not os.path.exists(dir):
                os.makedirs(dir)
        for i in data['playlist']['tracks']:
            id = i['id']
            album = i['albums'][0]['id']
            tr = Track(default_path=dir + '/')
            tr.download(id, album)
