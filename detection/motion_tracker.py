#!/usr/bin/python
"""
This SimpleCV example uses a technique called frame differencing to determine
if motion has occurred.  You take an initial image, then another, subtract
the difference, what is left over is what has changed between those two images
this are typically blobs on the images, so we do a blob search to count
the number of blobs and if they exist then motion has occurred
"""
import time
from simplecv.api import Camera, Blob

cam = Camera()  # setup the camera

# settings for the project
# make the threshold adaptable for various camera sizes
min_size = 0.1 * cam.get_property("width") * cam.get_property("height")
thresh = 10  # frame diff threshold
show_message_for = 2  # the amount of seconds to show the motion detected message
motion_timestamp = int(time.time())
message_text = "Motion detected"
draw_message = False

last_img = cam.get_image()
last_img.show()

while True:
    new_img = cam.get_image()
    track_img = new_img - last_img  # diff the images
    blobs =  track_img.find(Blob)  # use adaptive blob detection
    now = int(time.time())

    # If blobs are found then motion has occurred
    if blobs:
        motion_timestamp = now
        draw_message = True

    # See if the time has exceeded to display the message
    if (now - motion_timestamp) > show_message_for:
        draw_message = False

    # Draw the message on the screen
    if draw_message:
        new_img.dl().text(message_text, (5, 5))
        print message_text

    last_img = new_img  # update the image
    new_img.show()
