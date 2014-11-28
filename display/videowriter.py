#!/usr/bin/python

from simplecv.api import Camera
from simplecv.stream import VideoStream
import time

c = Camera()
vs = VideoStream("foo.avi")

for i in range(0, 500):
    c.get_image().edges().invert().save(vs)
    time.sleep(0.05)
