"""
This example finds a quarter in the picture and then uses that measurement
to determine the rest of the coins in the picture.  Since a quarter is always
a certain size we can use it as a reference because it is known.

In this example we use millimeters to pixels to do the conversion.

The sizes of coins are as follows:
penny - 19.05 mm
nickel - 21.21 mm
dime - 17.9 mm
quarter - 24.26 mm

"""
import time

from simplecv.api import Image, Color, Blob


print __doc__

# A quarter is 24.26mm or 0.955in
quarter_size = 24.26  # millimeters

# This will hold the ratio of the image size to a quarter's actual size
size_ratio = 0

img = Image('coins.jpg', sample=True)
coins = img.invert().find(Blob, minsize=200)

# Here we compute the scale factor
if coins:
    c = coins[-1]
    diameter = c.radius * 2
    size_ratio = quarter_size / diameter

# Now we print the measurements back on the picture
for coin in coins:
    # get the physical size of the coin
    size = (coin.radius * 2) * size_ratio
    # label the coin accordingly
    if 18 < size < 20:
        coin_type = "penny"
    elif 20 < size < 23:
        coin_type = "nickel"
    elif 16 < size < 18:
        coin_type = "dime"
    elif 23 < size < 26:
        coin_type = "quarter"
    else:
        coin_type = "unknown"

    text = "Type: {}, Size: {}mm".format(coin_type, size)
    img.dl().text(text, (coin.x + 45, coin.y + 45), color=Color.BLUE)

img.show()
time.sleep(10)
