#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 03:21:51 2019

@author: lowsiowmeng
"""

from classes import photo
from statistics import median
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
    tagFreq = {}
    for line in lines:
        if i > 0:
            photo_info = line.split(' ')
            orientation = photo_info[0]
            tag_num = int(photo_info[1])
            tags = []
            for j in range(tag_num):
                tagName = photo_info[2+j].rstrip()
                if tagName in tagFreq:
                    tagFreq[tagName] += 1
                else:
                    tagFreq[tagName] = 1
                tags.append(tagName)
            photo_id = i - 1
            if orientation == 'H':
                hPhotos.append(photo(photoID=photo_id,orient=orientation,tags = tags))
            elif orientation == 'V':
                vPhotos.append(photo(photoID=photo_id,orient=orientation,tags = tags))
        i += 1
    
    allFScores = []
    hPhotosNumTags = []
    hPhotosTagsFScores = []
    for k in range(len(hPhotos)):
        numTags = 0
        tagsWSums = 0
        
        for tag in hPhotos[k].tags:
            tagsWSums += tagFreq[tag]
            numTags += 1
        
        hPhotos[k].tagsFScore = tagsWSums / numTags
        allFScores.append(hPhotos[k].tagsFScore)
        hPhotosNumTags.append(len(hPhotos[k].tags))
        hPhotosTagsFScores.append(hPhotos[k].tagsFScore)
    
    vPhotosNumTags = []
    vPhotosTagsFScores = []
    for k in range(len(vPhotos)):
        numTags = 0
        tagsWSums = 0
        
        for tag in vPhotos[k].tags:
            tagsWSums += tagFreq[tag]
            numTags += 1
        
        vPhotos[k].tagsFScore = tagsWSums / numTags
        allFScores.append(vPhotos[k].tagsFScore)
        vPhotosNumTags.append(len(vPhotos[k].tags))
        vPhotosTagsFScores.append(vPhotos[k].tagsFScore)
    
    return hPhotos, hPhotosNumTags, hPhotosTagsFScores, vPhotos, vPhotosNumTags, vPhotosTagsFScores, median(allFScores)
