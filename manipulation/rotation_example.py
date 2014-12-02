#!/usr/bin/python
"""
This example shows how to perform various rotations and warps on images
and put back into a display.
"""
print __doc__

import time
from simplecv.api import Color, Image


sleep_for = 3  # seconds to sleep for
text_point = (20, 20)
font_size = 24
draw_color = Color.YELLOW

while True:
    image = Image("orson_welles.jpg", sample=True)
    image.dl().set_font_size(font_size)
    image.dl().text("Original Size", text_point, color=draw_color)
    image.show()
    time.sleep(sleep_for)

    rot = image.rotate(45)
    rot.dl().set_font_size(font_size)
    rot.dl().text("Rotated 45 degrees", text_point, color=draw_color)
    rot.show()
    time.sleep(sleep_for)

    rot = image.rotate(45, scale=0.5)
    rot.dl().set_font_size(font_size)
    rot.dl().text("Rotated 45 degreesand scaled", text_point, color=draw_color)
    rot.show()
    time.sleep(sleep_for)

    rot = image.rotate(45, scale=0.5, point=(0, 0))
    rot.dl().set_font_size(font_size)
    rot.dl().text("Rotated 45 degrees and scaled around a point", text_point, color=draw_color)
    rot.show()
    time.sleep(sleep_for)

    rot = image.rotate(45, "full")
    rot.dl().set_font_size(font_size)
    rot.dl().text("Rotated 45 degrees and full", text_point, color=draw_color)
    rot.show()
    time.sleep(sleep_for)

    atrans = image.shear([(image.width / 2, 0),
                          (image.width - 1, image.height / 2),
                          (image.width / 2, image.height - 1)])
    atrans.dl().set_font_size(font_size)
    atrans.dl().text("Affine Transformation", text_point, color=draw_color)
    atrans.show()
    time.sleep(sleep_for)

    ptrans = image.warp([(image.width * 0.05, image.height * 0.03),
                         (image.width * 0.9, image.height * 0.1),
                         (image.width * 0.8, image.height * 0.7),
                         (image.width * 0.2, image.height * 0.9)])
    ptrans.dl().set_font_size(font_size)
    ptrans.dl().text("Perspective Transformation", text_point, color=draw_color)
    ptrans.show()
    time.sleep(sleep_for)
