#!/usr/bin/env python3

import argparse
import random
import sys
import os
import time
import subprocess

def setWallpaper(img):
        print('Setting wallpaper to {0}'.format(img))
        p = subprocess.Popen(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', 'file://'+img], stdout=None, stdin=None, stderr=None)
        p.communicate()

def setWallpaperFb(img):
        print('Setting wallpaper to {0}'.format(img))
        p = subprocess.Popen(['fbsetbg', '-a', img], stdout=None, stdin=None, stderr=None)
        p.communicate()

parser = argparse.ArgumentParser(description='Random background from image folder.')
parser.add_argument('--folder', dest='folder', help='Folder containing the pictures')
parser.add_argument('--method', dest='method', help='Background switch method (default: gnome settings).', default='gnome', choices=['gnome', 'fb'])

args = parser.parse_args()

method=setWallpaper if args.method == 'gnome' else setWallpaperFb

allowedExts = ['.png', '.jpg', 'bmp', '.tiff']
interval = 30

if args.folder is None:
    folder = os.path.join(os.getenv('HOME'), 'Pictures', 'Wallpapers')
    print('No folder specified: using {0}'.format(folder))
else:
    folder = os.path.abspath(sys.argv[0])

print('Reading from {0}'.format(folder))
imgs=[]
for root, dirs, files in os.walk(folder):
	for name in files:
		i = os.path.join(root, name)
		if os.path.splitext(i)[1] in allowedExts: # And more
			imgs.append(i)

if len(imgs) == 0:
	print('No images found in {0}! Exiting.'.format(folder))
	sys.exit(0)
else:
	print('Found {0} images.'.format(len(imgs)))

random.seed(None)

while True:
	method(random.choice(imgs))
	time.sleep(interval)



