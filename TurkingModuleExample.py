# This example shows how to use the turking module.
# by turking we mean manually sorting and classifying images
# ostensibly for supervised learning

from simplecv.color import Color
from simplecv.machine_learning.turking_module import TurkingModule


# return images of all the big blobs in our source images
def preprocess(img):
    blobs = img.find_blobs(minsize=200)
    blobs = blobs.sort_area()
    return [b.img for b in blobs]


# once we are done invert them
def postprocess(img):
    return img.invert()


# we are going to turk two things junk and stuff
classes = ['junk', 'stuff']
# press j for junk and s for stuff
key_bind = ['j', 's']
# put stuff right here
outdir = './'
# use the sample images directory for our sources
input = ['../simplecv/data/sampleimages/']

# set everything up
turker = TurkingModule(input, outdir, classes, key_bind, preprocess, postprocess)

# run the turking, the display window must have focus
turker.turk(font_size=16, color = Color.BLUE, spacing=18)

# show what we got
print "="*30
print "TURKING DONE!"
for c in classes:
    print "="*30
    print "Showing " + c
    iset = turker.get_class(c)
    iset.show(0.1)

# save the results
turker.save('junkAndStuff.pkl')
