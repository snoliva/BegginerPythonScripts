#!/usr/bin/env python3
# Importing Library
import os
import argparse
from PIL import Image
# Base Path (Actual Folder)
base_folder = os.path.dirname(__file__)
image_path= os.path.join(base_folder, 'images')

if not os.path.exists(image_path):
    os.makedirs(image_path)

parser = argparse.ArgumentParser(description='Resize and convert format image')
parser.add_argument("-f", "--format", help="Format to save image. Default GIF", type=str, default="gif")
parser.add_argument("-s", "--size", help="Size of image. Type NumberxNumber. Default 500x300", type=str, default="500x300")
parser.add_argument("-p", "--path", help="Path of Image", type=str)

args = parser.parse_args()

print(args.format.lower())
print(args.size)
size = args.size.split("x")
formats = ["jpg", "gif", "png"]
# Loading the image
image = Image.open(args.path)
image.thumbnail((int(size[0]),int(size[1])))
# image.resize((20,20))
print(image.size)
# image.resize((int(size[0]), int(size[1])),Image.ANTIALIAS)
 
# Converting image from JPG to PNG format
# if args.format:
image.save(image_path+"/imageresize."+args.format.lower())
print("Image successfully converted!\n")
print("Image saved "+image_path+"/imageresize."+args.format.lower())