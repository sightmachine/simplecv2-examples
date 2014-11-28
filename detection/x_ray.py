#!/usr/bin/env python
# 
# Released under the BSD license. See LICENSE file for details.
"""
This program basically overlays an edge detector window that gives the
illusion of X-ray vision.  It is mearly meant to show how to perform a
basic image operation and overlay back onto the original image.
"""
print __doc__

from simplecv.api import Camera

# Initialize the camera
cam = Camera()

# Loop forever
while True:
    # Grab image from camera and flip it
    img = cam.get_image().flip_horizontal()

    # Set the x and the y location to scale
    crop_x = 50
    crop_y = 50
    crop_width = img.width - 100
    crop_height = img.height - 100

    # Crop out the section of image we want
    cropped_img = img.crop(crop_x, crop_y, crop_width, crop_height)
    # Get the edges of cropped region 
    xray_img = cropped_img.edges().smooth()
    # Draw the cropped image onto the current image
    img.dl().blit(xray_img.to_bgr(), (crop_x, crop_y))
    # Display the image
    img.show()
