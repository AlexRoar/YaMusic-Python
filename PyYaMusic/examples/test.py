#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#

from PyYaMusic.playlist import Playlist
from PyYaMusic.metadata import Metadata

# t = Track()
# # t.getTrackInfo('52303087','7355880')
# t.search('Jenny of Oldstones')
# t.downloadFirst()

# p = Playlist('1141', 'RollingStoneRussia')
# p.downloadAll()

meta = Metadata('/Users/aleksandrdremov/Music/iTunes/iTunes Media/Music')
meta.allMetaDataInDir(recursively=True, prompt=False)
