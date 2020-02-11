#  Copyright (c) 2020.
#  Designed and codded with love by Aleksander Dremov
#
#

import requests

cookies = {}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://music.yandex.ru/users/Dremov11112/playlists/777',
    'X-Current-UID': '227207001',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://music.yandex.ru',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://music.yandex.ru/users/Dremov11112/playlists/777',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = {
    'entries': '9330:8313,10277791:1111262,3616431:625175,64218:2494415,6687684:718991,2297105:3015881,1706655:282361,3616441:625175,14628171:1598845,3616437:625175,818304:421063,89287:10811,4299414:496033,6687694:718991,68684:7112,18524451:2061786,18399526:2732600,483388:51178,4299418:496033,2833983:642934,18398363:2732600,120142:11322,17079396:3060154,10270285:1110518,64220:3015881,2391186:236379,21515454:2818497,14521131:1585407,14145383:1726023,3591615:625175,14212213:1973727,10814889:1585407,1706660:282361,366272:1910064,16304822:1781582,14937363:1671558,23900280:2770824,112728:10811,360946:51178',
    'strict': 'true',
    'lang': 'en',
    'experiments': '{"musicChartSwitch":"on","boostConfigExperiment5e037188d189cd0705a818f5":"on","musicNewGenres":"on","musicPrice":"default","boostConfigExperiment5df479d5293df5523e0a2e7e":"on","searchDoNotRemoveStopwords":"on","rotorSafeTopTracksCount":"twelve","musicExperimentalPlayer":"default","adv":"newMinimalBlock","rotorIosHappyNewYearDesign":"default","plusWebSale":"on","boostConfigExperiment5dc5a44a8ab61649c7f0a115":"default","musicCrackdownPopup":"on","strm":"default","ugcPrivat":"on","webAutoPlaylistAnimated":"on","musicArtistDetailInfo":"default","boostConfigExperiment5dea42390060757a86beb5cd":"default","searchPrioritizeOwnContent":"on","boostConfigExperiment5cb9e691b0b921165380c369":"on","webNewPlaylistsTabHide":"hidden","boostConfigExperiment5dfc94111f183806f3373f4f":"on","branchLinks":"on","webAntiMusicTab":"on","musicTouchNewPleer":"on","webBughunter":"default","musicCspLogger":"default","searchWizardParameters":"default","musicCollectivePlaylist":"on","musicCheckPass":"on","boostConfigExperiment5e2835e484d6895476a1e866":"on","webPlaylistOfTheDayCounter":"on","miniBrick":"advFixed","musicUzbekistanLang":"on","searchQuorumSoftness":"soft","webSidebarPodcastbanner":"default","musicSearchRanking":"new-toloka-0.9-ann","djvuCandidates":"daily_based_neverheard","webAutoplaylistsOnMain":"on","musicSuggest":"on","musicFamilyLanding":"on","windowsEqualizer":"default","searchPrioritizeLikes":"default","music30SecToMars":"on","webSimilarArtistsInHead":"on","musicMobileWebLocked":"play","musicYellowButtonAuth":"on","musicLandingIntentPlaylistCount":"default","musicArmeniaLang":"on","rotorNewSettings":"on","musicTestDebugProducts":"default","webMusicPreroll":"on","musicVideoOnArtistPage":"on","musicLoginWall":"tracks-0","webPPbanners":"white0t3","boostConfigExperiment5df47997293df5523e0a2e6f":"default","musicLoginWallElapse":"0","musicCryMeARiver":"on","searchDisableDisamb":"default","musicCrackdownContent":"default","musicHebrewLang":"default","boostConfigExperiment5df47980293df5523e0a2e68":"on","musicTakeEMail":"on","webAntiMusicBlockNaGlavnoi":"on","musicgift":"custom_2","musicYellowButton":"on","feedTriggers":"default","webPodcastShowUpdated":"default","boostConfigExperiment5dc5a3ef8ab61649c7f0a105":"on","SubStation":"day1604","plusWeb":"on","musicSyncQueue":"default","musicKazakhstanLang":"on","musicStatsLogger":"default","BlockOrderByRelevanceWeb":"on","boostConfigExperiment5cb9e0aa7cfafa58d9db3914":"default","musicHighlightLyrics":"default","boostConfigExperiment5df479fe293df5523e0a2e86":"on","firstPlaylistLikesCheck":"default","boostConfigExperiment5df4794f293df5523e0a2e5f":"on","searchPremiumContentForAll":"on","musicArtistStat":"on","boostConfigExperiment5df479b4293df5523e0a2e77":"default","ugc":"on-upload","musicNoFeed":"on","musicAutoFlow":"default","musicLoginPopup":"on","userFeed":"feed_october_streams_potd_rank_formula_with_play_skips","boostConfigExperiment5e3c13f1727a810cbd38d182":"on","musicErrorLogger":"default","audioAdsWhite":"on"}',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false'
}

print(requests.post('https://music.yandex.ru/handlers/track-entries.jsx', headers=headers, cookies=cookies,
                    data=data).text)
