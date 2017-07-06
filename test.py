#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import shutil
import os
import time

image_dic = [
    [512, "iTunesArtwork.png"],
    [1024, "iTunesArtwork@2x.png"],
    [120, "Icon-60@2x.png"],
    [180, "Icon-60@3x.png"],
    [76, "Icon-76.png"],
    [152, "Icon-76@2x.png"],
    [167, "Icon-83.5@2x.png"],
    [40, "Icon-Small-40.png"],
    [80, "Icon-Small-40@2x.png"],
    [120, "Icon-Small-40@3x.png"],
    [29, "Icon-Small.png"],
    [58, "Icon-Small@2x.png"],
    [87, "Icon-Small@3x.png"]
]

def create_icon(file_icon = "icon.png"):
    if not os.path.exists("output"): os.mkdir("output")

    file_dir = "output/"+time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    os.makedirs(file_dir)
    for i in image_dic:
        size = i[0]
        file_name = i[1]
        pri_image = Image.open(file_icon)
        pri_image.resize((size, size), Image.ANTIALIAS).save( "%s/%s" % (file_dir, file_name))
    shutil.copy(file_icon,file_dir)

if __name__ == "__main__": create_icon()
