#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#
import requests
from PyYaMusic.track import Track
import json
import urllib.parse
from tqdm import tqdm

class Album:

    def __init__(self, album_id):
        self.album_id = album_id

    def getInf(self):

        cookies = {}

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Retpath-Y': 'https://music.yandex.ru/artist/675068/albums',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
            'X-Current-UID': '227207001',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://music.yandex.ru/artist/675068/albums',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        }

        params = (
            ('album', self.album_id),
            ('lang', 'en'),
            ('external-domain', 'music.yandex.ru'),
            ('overembed', 'false'),
            ('ncrnd', '0.6828676435565784'),
        )


        response = requests.get('https://music.yandex.ru/handlers/album.jsx', headers=headers, params=params,
                                cookies=cookies)
        data = json.loads(response.content)
        self.title = data['title']
        out = []
        for i in data['volumes']:
            for j in i:
                out.append(j['id'])
        return out

    def downloadAll(self):
        tracks = self.getInf()

        name = urllib.parse.quote(self.title, safe='')

        for i in tqdm(range(len(tracks))):
            i = tracks[i]
            tr = Track(name)
            tr.download(i,self.album_id)

