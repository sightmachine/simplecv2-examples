import cv2
from simplecv.segmentation.color_segmentation import ColorSegmentation
from simplecv.api import Color, Image
from simplecv.ui import Window


class ColorSegmentationWindow(Window):

    def __init__(self):
        super(ColorSegmentationWindow, self).__init__('Color Segmentation Example')
        self.img = Image('simplecv')
        self.segmentation = ColorSegmentation()
        self.normal = True  # mode toggle for segment detection
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
                crop = self.img.crop(x1, y1, w, h)
                self.segmentation = ColorSegmentation()
                self.segmentation.add_to_model(crop)

    def on_key(self, key):
        if key == 32:  # Space bar to switch between modes
            self.normal = not self.normal
            print "Display Mode:", "Normal" if self.normal else "Segmented"

    def on_update(self):
        """ Callback for periodic update.
        """
        if self.normal:
            self.img.clear_layers()
            self.img.dl().rectangle_to_pts(self.point1, self.point2, color=Color.RED)
            self.show(self.img.apply_layers())
        else:
            self.segmentation.add_image(self.img)
            if self.segmentation.is_ready():
                img = self.segmentation.get_segmented_image()
                img = img.erode(iterations = 2).dilate().invert()
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
