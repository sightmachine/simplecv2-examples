"""
This example uses the built in template matching.  The easiest way
to think of this is if you played the card matching game, the cards would
pretty much have to be identical.  The template method doesn't allow much
for the scale to change, nor for rotation.  This is the most basic pattern
matching SimpleCV offers.  If you are looking for something more complex
you will probably want to look into img.find()
"""
print __doc__

import time

from simplecv.api import Image, Color, TemplateMatch


source = Image("templatetest.png", sample=True) # the image to search
template = Image("template.png", sample=True) # the template to search the image for
t = 5

methods = ["SQR_DIFF", "SQR_DIFF_NORM", "CCOEFF",
           "CCOEFF_NORM", "CCORR", "CCORR_NORM"]  # the various types of template matching available

for m in methods:
    img = Image("templatetest.png", sample=True)
    img.dl().text("current method: {}".format(m), (10, 20), color=Color.RED)
    fs = source.find(TemplateMatch, template, threshold=t, method=m)
    for match in fs:
        img.dl().rectangle((match.x, match.y), (match.width, match.height), color=Color.RED)
    img.apply_layers().show()
    time.sleep(3)
