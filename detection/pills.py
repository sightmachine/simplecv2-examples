"""
This demo is used to find missing pills in a blister type of package
it would be used in quality control in manufacturing type of application
were you are verifying that the correct number of pills are present
"""

from simplecv.api import Image, Color, Blob

pillcolor = (153, 198, 252)  # This is set manually, you could either open the image you want and pick the color, or use blob detection to find the blob and do .mean_color() to get the RGB value
i = Image("pills.png", sample=True)
expected_pillcount = 12
saturation_threshold = 40  # This is how much saturation to allow in the image
pill_size = 100 # The size of the expected pills in pixels
packblobs = i.find(Blob, minsize=10) #find the bright silver on back blackground, easy


# run through the list of pills (blobs) found and check their color and markup the image when they are found
for idx in range(len(packblobs)):
    pack = packblobs[idx].crop()

    pills_img = pack.hue_distance(pillcolor, minsaturation=saturation_threshold)
    pills_img = pills_img.binarize(127, inverted=True)

    pills = pills_img.find(Blob, minsize=pill_size)
    if not pills:
        continue

    for p in pills:
        p.image = pack
        p.convex_hull.draw(color=Color.RED, width=5)
    i.dl().blit(pack.apply_layers(), packblobs[idx].points[0])
    packblobs[idx].convex_hull.draw(color=Color.BLUE, width=5)

    pillcount = len(pills)
    if pillcount != expected_pillcount:
        print "pack at %d, %d had %d pills" % (packblobs[idx].x, packblobs[idx].y, pillcount)
        i.dl().text('ERROR', (packblobs[idx].x, packblobs[idx].y + 150), color=Color.RED)
        i.dl().text("Pills Found: " + str(pillcount),
                    (packblobs[idx].x, packblobs[idx].y + 170), color=Color.RED)
        i.dl().text("Pills Expected: " + str(expected_pillcount),
                    (packblobs[idx].x, packblobs[idx].y + 190), color=Color.RED)
    else:
        i.dl().text('OK', (packblobs[idx].x, packblobs[idx].y + 150), color=Color.GREEN)


#Continue to show the image
while True:
    i.show()

