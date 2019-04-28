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

m = Metadata('/Users/aleksandrdremov/PycharmProjects/YaMusic-Python/PyYaMusic/examples/Премьера')
m.allMetaDataInDir()
