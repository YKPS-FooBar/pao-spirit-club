import glob
import os
import sys

from PIL import Image


width = int(sys.argv[1]) if len(sys.argv) == 2 else 768

for infile in glob.glob('photos/*/*.*'):
    outpath = os.path.join(
        'photos/thumbnails',
        # 1 for the first 'photos' and -1 for removing file name
        *infile.split(os.path.sep)[1:-1]
    )
    outfile = os.path.join(outpath, os.path.split(infile)[1])
    if not os.path.isfile(outfile):
        os.makedirs(outpath, exist_ok=True)
        im = Image.open(infile)
        im.thumbnail((width, width))
        im.save(outfile)
