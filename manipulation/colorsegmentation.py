#!/usr/bin/python
"""
This program uses a Color model to try and do segmentation based on color
"""

print __doc__

import time
from simplecv.color_model import ColorModel
from simplecv.api import Camera

c = Camera()
i = c.get_image()
cm = ColorModel(i)
i.show()
t = int(time.time())
ticks = 0

while True:
    cm.threshold(c.get_image()).show()
    time.sleep(0.01)
    ticks = ticks + 1
    if int(time.time()) > t:
        print str(ticks) + " fps"
        ticks = 0
        t = int(time.time())
