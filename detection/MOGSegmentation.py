from simplecv.api import Camera, Image
from simplecv.color import Color
from simplecv.segmentation.mog_segmentation import MOGSegmentation

mog = MOGSegmentation(history=200, mixtures=5, bg_ratio=0.3, noise_sigma=16,
                      learning_rate=0.3)

frame = Image('lenna')

mog.add_image(frame)

segmented_image = mog.get_segmented_image()
blobs = mog.get_segmented_blobs()
for blob in blobs:
    segmented_image.dl().circle((blob.x, blob.y), 10, Color.RED)

segmented_image.show()
