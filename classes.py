#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 02:10:18 2019

@author: lowsiowmeng
"""

# Input Class: List of Photos
class photo():
    
    def __init__(self, orient, tags):
        
        self.orient = orient
        self.tags = tags

# Output Class: List of Slides
class slide():
    
    def __init__(self, slideType, photos, tags):
        
        self.slideType = slideType
        self.photos = photos
        
        self.tags = set([])
        
        for photo in self.photos:
            self.tags = self.tags.union(photo.tags)


