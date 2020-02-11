#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#
import requests
import json
from PyYaMusic.track import Track
from tqdm import tqdm
from copy import deepcopy


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
            'X-Retpath-Y': 'https://music.yandex.ru/users/' + owner + '/playlists/' + id,
            'X-Current-UID': '227207001',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://music.yandex.ru/users/' + owner + '/playlists/' + id,
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

        final = json.loads(response.text)
        prevRequest = deepcopy(final['playlist']['tracks'])
        already = set()

        entries = ''
        for i in range(len(prevRequest)):
            i = prevRequest[i]
            id = i['id']
            album = i['albums'][0]['id']
            idEnt = str(id) + ':' + str(album)
            already.add(idEnt)
            entries += ','+idEnt
        entries = entries[1:]
        data = {
                'entries': entries,
                'strict': 'true',
                'lang': 'en',
                'experiments': '{"musicChartSwitch":"on","boostConfigExperiment5e037188d189cd0705a818f5":"on","musicNewGenres":"on","musicPrice":"default","boostConfigExperiment5df479d5293df5523e0a2e7e":"on","searchDoNotRemoveStopwords":"on","rotorSafeTopTracksCount":"twelve","musicExperimentalPlayer":"default","adv":"newMinimalBlock","rotorIosHappyNewYearDesign":"default","plusWebSale":"on","boostConfigExperiment5dc5a44a8ab61649c7f0a115":"default","musicCrackdownPopup":"on","strm":"default","ugcPrivat":"on","webAutoPlaylistAnimated":"on","musicArtistDetailInfo":"default","boostConfigExperiment5dea42390060757a86beb5cd":"default","searchPrioritizeOwnContent":"on","boostConfigExperiment5cb9e691b0b921165380c369":"on","webNewPlaylistsTabHide":"hidden","boostConfigExperiment5dfc94111f183806f3373f4f":"on","branchLinks":"on","webAntiMusicTab":"on","musicTouchNewPleer":"on","webBughunter":"default","musicCspLogger":"default","searchWizardParameters":"default","musicCollectivePlaylist":"on","musicCheckPass":"on","boostConfigExperiment5e2835e484d6895476a1e866":"on","webPlaylistOfTheDayCounter":"on","miniBrick":"advFixed","musicUzbekistanLang":"on","searchQuorumSoftness":"soft","webSidebarPodcastbanner":"default","musicSearchRanking":"new-toloka-0.9-ann","djvuCandidates":"daily_based_neverheard","webAutoplaylistsOnMain":"on","musicSuggest":"on","musicFamilyLanding":"on","windowsEqualizer":"default","searchPrioritizeLikes":"default","music30SecToMars":"on","webSimilarArtistsInHead":"on","musicMobileWebLocked":"play","musicYellowButtonAuth":"on","musicLandingIntentPlaylistCount":"default","musicArmeniaLang":"on","rotorNewSettings":"on","musicTestDebugProducts":"default","webMusicPreroll":"on","musicVideoOnArtistPage":"on","musicLoginWall":"tracks-0","webPPbanners":"white0t3","boostConfigExperiment5df47997293df5523e0a2e6f":"default","musicLoginWallElapse":"0","musicCryMeARiver":"on","searchDisableDisamb":"default","musicCrackdownContent":"default","musicHebrewLang":"default","boostConfigExperiment5df47980293df5523e0a2e68":"on","musicTakeEMail":"on","webAntiMusicBlockNaGlavnoi":"on","musicgift":"custom_2","musicYellowButton":"on","feedTriggers":"default","webPodcastShowUpdated":"default","boostConfigExperiment5dc5a3ef8ab61649c7f0a105":"on","SubStation":"day1604","plusWeb":"on","musicSyncQueue":"default","musicKazakhstanLang":"on","musicStatsLogger":"default","BlockOrderByRelevanceWeb":"on","boostConfigExperiment5cb9e0aa7cfafa58d9db3914":"default","musicHighlightLyrics":"default","boostConfigExperiment5df479fe293df5523e0a2e86":"on","firstPlaylistLikesCheck":"default","boostConfigExperiment5df4794f293df5523e0a2e5f":"on","searchPremiumContentForAll":"on","musicArtistStat":"on","boostConfigExperiment5df479b4293df5523e0a2e77":"default","ugc":"on-upload","musicNoFeed":"on","musicAutoFlow":"default","musicLoginPopup":"on","userFeed":"feed_october_streams_potd_rank_formula_with_play_skips","boostConfigExperiment5e3c13f1727a810cbd38d182":"on","musicErrorLogger":"default","audioAdsWhite":"on"}',
                'external-domain': 'music.yandex.ru',
                'overembed': 'false'
        }

        prevRequest = json.loads(
                requests.post('https://music.yandex.ru/handlers/track-entries.jsx', headers=headers, cookies=cookies,
                              data=data).text)

        final = json.loads(response.text)
        # print(final['playlist']['trackIds'])
        return final

    def downloadAll(self, dir='auto'):
        data = self.get_inf()
        if (dir == 'auto'):
            dir = data['playlist']['title']
            import os
            if not os.path.exists(dir):
                os.makedirs(dir)
        for i in tqdm(range(len(data['playlist']['trackIds']))):
            i = data['playlist']['trackIds'][i]
            tmp = i.split(':')
            id = tmp[0]
            album = tmp[1]
            tr = Track(default_path=dir + '/')
            tr.download(id, album)
