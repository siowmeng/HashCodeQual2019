#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 02:10:18 2019

@author: lowsiowmeng
"""

from itertools import combinations

# Input Class: List of Photos
class photo():
    
    def __init__(self, photoID, orient, tags):
        
        self.photoID = photoID
        self.orient = orient
        self.tags = tags

# Output Class: List of Slides
class slide():
    
    def __init__(self, slideType, photos):
        
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

def getVCombi(vPhotos):
    vCombi = combinations(range(len(vPhotos)), 2)
    
    vSlidesCandidates = [None] * len(vPhotos)
    vSlidesBestTags = [0] * len(vPhotos)
    vSlidesBestPairs = [-1] * len(vPhotos)
    for idx1, idx2 in vCombi:
        currSlide = slide('V', [vPhotos[idx1], vPhotos[idx2]])
        if len(currSlide.tags) > vSlidesBestTags[idx1]:
            vSlidesCandidates[idx1] = currSlide
            vSlidesBestTags[idx1] = len(currSlide.tags)
            vSlidesBestPairs[idx1] = idx2
        if len(currSlide.tags) > vSlidesBestTags[idx2]:
            vSlidesCandidates[idx2] = currSlide
            vSlidesBestTags[idx2] = len(currSlide.tags)
            vSlidesBestPairs[idx2] = idx1
    
    return vSlidesCandidates, vSlidesBestTags, vSlidesBestPairs

def findCombi(listPhotos):
#    vPhotoID = []
#    vPhotoTags = []
    vPhotos = []
#    hPhotoID = []
#    hPhotoTags = []
    hPhotos = []
    
    for photo in listPhotos:
        if photo.orient == 'H':
#            hPhotoID.append(photo.photoID)
#            hPhotoTags.append(photo.tags)
            hPhotos.append(photo)
        elif photo.orient == 'V':
#            vPhotoID.append(photo.photoID)
#            vPhotoTags.append(photo.tags)
            vPhotos.append(photo)
    
    vCombi = combinations(range(len(vPhotos)), 2)
    
    vSlidesCandidates = []
    for idx1, idx2 in vCombi:
        vSlidesCandidates.append(slide('V', [vPhotos[idx1], vPhotos[idx2]]))
    
    hSlidesCandidates = []
    for photo in hPhotos:
        hSlidesCandidates.append(slide('H', [photo]))
    
    return hSlidesCandidates, vSlidesCandidates
