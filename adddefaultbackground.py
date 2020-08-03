import os
from shutil import *
from plistlib import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("background")
args = parser.parse_args()

backgroundname = args.background.split("/")[len(args.background.split("/"))-1]

with open("/System/Library/Desktop Pictures/.orderedPictures.plist", 'rb') as plistFile:
    backgroundsPlist = load(plistFile)

print(" ")
print("This script need to be run as root!")
print(" ")
print("Adding " + backgroundname + " to default wallpapers")
print(" ")
copyfile(args.background, "/System/Library/Desktop Pictures/" + backgroundname)
copyfile(args.background, "/System/Library/Desktop Pictures/.thumbnails/" + backgroundname)
backgroundsPlist.append(backgroundname)

with open("/System/Library/Desktop Pictures/.orderedPictures.plist", 'wb') as plistFile:
    dump(backgroundsPlist, plistFile)
