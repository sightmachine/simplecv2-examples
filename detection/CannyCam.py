#!/usr/bin/python
'''
This example just takes an image, finds the edges, and draws them
the threshold is used for the edge detection, if you adjust the
max_threshold and threshold_step values and run the program you will
see it change over time
'''
print __doc__

from simplecv.api import Camera, Color

cam = Camera()  # initialize the camera
max_threshold = 255  # this is used for the edge detection
threshold_step = 0.5  # this is the amount to adjust the threshold by each time the display is updated
threshold = max_threshold

while True:
    image = cam.get_image() # get image (or frame) from camera
    flipped_image = image.flip_horizontal() # flip it so it looks mirrored
    edged_image = flipped_image.edges(threshold) # get the image edges

    # This just automatically cycles through threshold levels
    if threshold <= 0:
        threshold = max_threshold
    else:
        threshold = threshold - 0.5

    edged_image.draw_text("Current Edge Threshold:" + str(threshold), (10, 20), color=Color.GREEN)
    edged_image.show()
