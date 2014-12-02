#!/usr/bin/python
"""
This program basically simulates some kind of 80's music video.
"""
print __doc__


from simplecv.api import Camera, Blob


cam = Camera()

# settings for the project
min_size = 0.1 * cam.get_property("width") * cam.get_property("height")  # Change threshold
thresh = 10  # frame difference threshold

last_img = cam.get_image()
last_img.dl().text("Move around to get the party started!", (5, 5))
last_img.show()

while True:
    new_img = cam.get_image()
    track_img = new_img - last_img  # difference the images
    blobs =  track_img.find(Blob, -1, threshblocksize=99)  # use adapative blob detection
    if blobs:
        blobs.draw(autocolor=True)
        track_img.show()
    last_img = new_img # update the image
