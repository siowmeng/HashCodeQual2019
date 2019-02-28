#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 03:21:51 2019

@author: lowsiowmeng
"""

from classes import photo
#filepath = 'input/a_example.txt'

def num_of_photos(filename):
    lines = open(filename).readlines()
    N = int(lines[0].split()[0])
    
    return N

def input_parser(filepath):
    lines = open(filepath).readlines()
    i = 0
    hPhotos = []
    vPhotos = []
    for line in lines:
        if i > 0:
            photo_info = line.split(' ')
            orientation = photo_info[0]
            tag_num = int(photo_info[1])
            tags = []
            for j in range(tag_num):
                tags.append(photo_info[2+j].rstrip())
            photo_id = i - 1
            if orientation == 'H':
                hPhotos.append(photo(photoID=photo_id,orient=orientation,tags = tags))
            elif orientation == 'V':
                vPhotos.append(photo(photoID=photo_id,orient=orientation,tags = tags))
        i += 1
    return hPhotos, vPhotos
