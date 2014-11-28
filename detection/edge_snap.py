'''
This example illustrates the edgeSnap function in the Image class

Left-click to define points for snapping ( Blue )
Spacebar to clear points

'''
print __doc__

import cv2
from simplecv.api import Color, Image
from simplecv.ui import Window



class EdgeSnapWindow(Window):

    def __init__(self):
        super(EdgeSnapWindow, self).__init__('Color Segmentation Example')
        self.image = Image("shapes.png", sample=True).edges()
        self.points = []

        self.show(self.image)

    def on_mouse(self, event, x, y, mouse_key, data=None):
        """ Callback for mouse events

            event - int - see cv2.EVENT_* constants
            x, y - int, int - position of the cursor
            mouse_key - int - mouse key
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            self.points.append((x, y))

            self.image.clear_layers()
            for p in self.points:
                self.image.dl().circle(p, 5, color=Color.BLUE)

            features = self.image.edge_snap(self.points)

            for f in features:
                f.draw(color=Color.RED, width=2)

            self.show(self.image.apply_layers())

    def on_key(self, key):
        if key == 32:  # Space bar to clear points
            self.points = []
            self.image.clear_layers()
            self.show(self.image)
            print "Points cleared"


if __name__ == "__main__":
    w = EdgeSnapWindow()
    w.event_loop()

