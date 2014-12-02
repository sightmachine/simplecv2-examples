"""
This examples demonstrates the motionBlur method.
Use Up/Down Arrow keys to change power
Use Left/Right Arrow keys to change angle
"""
print __doc__

import time
import cv2
from simplecv.api import Image, Color
from simplecv.core.drawing.layer import DrawingLayer


img = Image((500, 500))
layer = DrawingLayer()
layer.set_font_size(25)

layer.rectangle((0, 0), (500, 500), Color.WHITE, 1, True)

# write the text
layer.text("Just some innocent looking dots", (50, 25), Color.BLACK)
layer.text("Use w/s keys to change intensity", (50, 50), Color.BLACK)
layer.text("a/d keys to change angle", (50, 75), Color.BLACK)

#draw 6 innocent looking dots
layer.circle((125, 200), 25, Color.RED, 1, True)
layer.circle((250, 200), 25, Color.BLUE, 1, True)
layer.circle((375, 200), 25, Color.GREEN, 1, True)
layer.circle((125, 300), 25, Color.YELLOW, 1, True)
layer.circle((250, 300), 25, Color.ORANGE, 1, True)
layer.circle((375, 300), 25, Color.CYAN, 1, True)

# apply layer
img.add_drawing_layer(layer)
img = img.apply_layers()

img.show()
power = 1
angle = 0
while True:
    key = cv2.waitKey(1)
    if key == -1:
        continue
    print chr(key)

    # detect w,a,s,d key presses and modify power, angle
    if key == ord('w'):
        power += 10
        blur = img.motion_blur2(power, angle)
        blur.show()
    if key == ord('s'):
        power = max(power - 10, 1)
        blur = img.motion_blur2(power, angle)
        blur.show()
    if key == ord('a'):
        angle -= 5
        blur = img.motion_blur2(power, angle)
        blur.show()
    if key == ord('d'):
        angle += 5
        blur = img.motion_blur2(power, angle)
        blur.show()
