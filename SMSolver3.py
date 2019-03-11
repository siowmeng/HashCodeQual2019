#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 02:39:06 2019

@author: lowsiowmeng
"""

from classes import slide, calcTransScores, calcSlideshowScores, getVCombi2
from parseInputSM import input_parser
from parseOutput import output_slideshow
import numpy as np

fname = 'b_lovely_landscapes'

hPhotos, hPhotosTags, hPhotosFScores, \
vPhotos, vPhotosTags, vPhotosFScores, \
medianFScore = input_parser('./Problem/' + fname + '.txt')

#vCandidates = getVCombi2(vPhotos)
hCandidates = []
for photo in hPhotos:
    hCandidates.append(slide('H', [photo]))

#hScores = [len(x.tags) for x in hCandidates]
#vScores = [len(x.tags) for x in vCandidates]

sortedIdx = list(np.argsort(hPhotosTags))

slideshow = []

popIdx = sortedIdx.pop()
slideshow.append(slide('H', [hPhotos[popIdx]]))
currNumTags = hPhotosTags[popIdx]
currFScore = hPhotosFScores[popIdx]

#popIdx = hPhotosTags.index(max(hPhotosTags))
#slideshow.append(hPhotos.pop(popIdx))
#currNumTags = hPhotosTags.pop(popIdx)
#currFScore = hPhotosFScores.pop(popIdx)

while len(sortedIdx) > 0:
    
    print(len(sortedIdx))
    currIdx = 0
    bestIdx = -1    
    bestScore = -1
    
    sortedIdxCopy = sortedIdx.copy()
    
    while len(sortedIdxCopy) > 0:
        
        nextPhotoIdx = sortedIdxCopy.pop()
        nextPhoto = hPhotos[nextPhotoIdx]
        nextNumTags = hPhotosTags[nextPhotoIdx]
        nextFScore = hPhotosFScores[nextPhotoIdx]
        
        if bestScore > 0:
            # First filter: number of tags
            if nextNumTags < (currNumTags / 2):
                break
            # Second filter: Frequent tags mix with scarce tags
            elif (currFScore > medianFScore) and (nextFScore > medianFScore):
                continue
            elif (currFScore <= medianFScore) and (nextFScore <= medianFScore):
                continue
        
        currScore = calcTransScores(slideshow[-1], nextPhoto)
        
        if currScore > bestScore:
            bestScore = currScore
            bestIdx = currIdx
        
        currIdx += 1
    
    bestSortedIdx = len(sortedIdx) - 1 - bestIdx
    popIdx = sortedIdx.pop(bestSortedIdx)
    slideshow.append(slide('H', [hPhotos[popIdx]]))
    currNumTags = hPhotosTags[popIdx]
    currFScore = hPhotosFScores[popIdx]
    
output_slideshow('./' + fname + '_solution.txt', slideshow)
print("Final Score: " + str(calcSlideshowScores(slideshow)))

