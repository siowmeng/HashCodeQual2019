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

def calcTransScores(slide1, slide2):
    
    numCommon = len(slide1.tags.intersection(slide2.tags))
    numDiff1 = len(slide1.tags.difference(slide2.tags))
    numDiff2 = len(slide2.tags.difference(slide1.tags))
    
    return min(numCommon, numDiff1, numDiff2)

def calcSlideshowScores(listSlides):
    
    prevSlide = None
    currSlide = None
    
    totalScore = 0
    for s in listSlides:
        prevSlide = currSlide
        currSlide = s
        
        if prevSlide == None:
            continue
        
        totalScore += calcTransScores(prevSlide, currSlide)
    
    return totalScore
    