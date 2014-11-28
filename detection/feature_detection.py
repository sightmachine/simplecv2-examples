#!/usr/bin/python
"""
This program is used to find keypoint features in an image.

You need to click the upper left hand corner of what you want to train,
then click the right lower corner of what you want to train.

This will give you a template.  For instance if you wanted to train
a face to recognize in the image you would click on the upper left corner
of the face, then click in the lower right corner of the face.  If you
want to retrain then just right click to reset.
"""
print __doc__


import cv2
from simplecv.api import Color, Camera
from simplecv.ui import Window


class ColorSegmentationWindow(Window):

    def __init__(self):
        super(ColorSegmentationWindow, self).__init__('Color Segmentation Example')
        self.cam = Camera()
        self.template_img = None
        self.point1 = (0, 0)
        self.point2 = (0, 0)
        self.mosue_down = False

    def on_mouse(self, event, x, y, mouse_key, data=None):
        """ Callback for mouse events

            event - int - see cv2.EVENT_* constants
            x, y - int, int - position of the cursor
            mouse_key - int - mouse key
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point1 = (x, y)
            self.point2 = (x, y)
            self.mosue_down = True
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.mosue_down == True:
                self.point2 = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            self.mosue_down = False
            self.point2 = (x, y)

            x1, y1, w, h = points_to_roi(self.point1, self.point2)
            if w > 0 and h > 0:
                self.template_img = self.cam.get_image().crop(x1, y1, w, h)
                print "Mode:", "Detecting features..."


    def on_key(self, key):
        if key == 32:  # Space bar to select template
            self.template_img = None
            print "Mode:", "Selecting template..."

    def on_update(self):
        """ Callback for periodic update.
        """
        img = self.cam.get_image()

        if self.mosue_down:
            img.dl().rectangle_to_pts(self.point1, self.point2, color=Color.RED)
            img = img.apply_layers()
        elif self.template_img is not None:
            # Detect and draw key points
            img = img.draw_keypoint_matches(self.template_img)
            img = img.apply_layers()

        self.show(img)


def points_to_roi(p1, p2):
    x = min(p1[0], p2[0])
    y = min(p1[1], p2[1])
    w = max(p1[0], p2[0]) - x
    h = max(p1[1], p2[1]) - y
    return x, y, w, h


if __name__ == "__main__":
    w = ColorSegmentationWindow()
    w.event_loop()