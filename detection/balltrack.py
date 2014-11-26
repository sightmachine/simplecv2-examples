"""
This is how to track a white ball example using SimpleCV

The parameters may need to be adjusted to match the RGB color
of your object.

"""
print __doc__

from simplecv.ui import Window
from simplecv.api import Camera, Color


class BallTrackWindow(Window):

    def __init__(self):
        super(BallTrackWindow, self).__init__('Ball Track Example')
        self.cam = Camera()  # initialize the camera
        self.normal = True  # mode toggle for segment detection

    def on_key(self, key):
        if key == 32:  # Space bar to switch between modes
            self.normal = not self.normal
            print "Display Mode:", "Normal" if self.normal else "Segmented"

    def on_update(self):
        """ Callback for periodic update.
        """
        img = self.cam.get_image().flip_horizontal()  # grab image from camera
        dist = img.color_distance(Color.BLACK).dilate(2)  # try to separate colors in image
        segmented = dist.stretch(200, 255)  # really try to push out white colors
        if not self.normal:
            img = segmented
        blobs = segmented.find_blobs()  # search the image for blob objects
        if blobs:  # if blobs are found
            circles = blobs.filter([b.is_circle(0.2) for b in blobs])  # filter out only circle shaped blobs
            if circles:
                # draw the circle on the main image
                img.dl().circle((circles[-1].x, circles[-1].y),
                                circles[-1].radius(), Color.BLUE, width=3)
        self.show(img.apply_layers())


if __name__ == "__main__":
    w = BallTrackWindow()
    w.event_loop()
