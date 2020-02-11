#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#

from PyYaMusic.track import Track

tr = Track('cache/')
tr.search('Dynasty Miia')
tr.downloadFirst()