"""
This program trys to extract the color pallette from an image
it could be used in machine learning as a color classifier
"""
print __doc__

from simplecv.api import Camera

cam = Camera()
count = 0
pal = None
while True:
    img = cam.get_image()
    if count % 10 == 0:
        temp = img.scale(0.3)
        p = temp.get_palette()
        pal = temp.draw_palette_colors(size=(640, 48))
    result = img.re_palette(p)
    result = result.side_by_side(pal, side='bottom')
    result.show()
    count = count + 1
