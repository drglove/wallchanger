import logging
import os
from random import shuffle
from glob import glob

# Put your directory of images (png and jpg only for now) here
dir = '/home/nlange/Pictures/Wallpapers/'
# Log changes to here
LOG_FILENAME = '/home/nlange/programming/wallchanger/changer.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logger = logging.getLogger('')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Get the list of images
images = glob(os.path.join(dir,'*.png'))
images.extend(glob(os.path.join(dir,'*.jpg')))

# Choose a random image
shuffle(images)
image = images[0]
logger.debug('%s' % image)

# Change the background
os.system('gconftool-2 --type string --set /desktop/gnome/background/picture_filename "%s"' % image)
logger.info('Successfully changed background\n')
