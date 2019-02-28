#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 02:39:06 2019

@author: lowsiowmeng
"""

from classes import slide, calcTransScores, getVCombi2
from parseInputSM import input_parser
from parseOutput import output_slideshow
import numpy as np

fname = 'd_pet_pictures'

hPhotos, vPhotos = input_parser('./Problem/' + fname + '.txt')
#hPhotos, vPhotos = input_parser('./Problem/a_example.txt')

#vCombi = combinations(range(len(vPhotos)), 2)
#    
#vSlidesCandidates = [None] * len(vPhotos)
#vSlidesBestTags = [0] * len(vPhotos)
#vSlidesBestPairs = [-1] * len(vPhotos)
#for idx1, idx2 in vCombi:
#    currSlide = slide('V', [vPhotos[idx1], vPhotos[idx2]])
#    if len(currSlide.tags) > vSlidesBestTags[idx1]:
#        vSlidesCandidates[idx1] = currSlide
#        vSlidesBestTags[idx1] = len(currSlide.tags)
#        vSlidesBestPairs[idx1] = idx2
#    if len(currSlide.tags) > vSlidesBestTags[idx2]:
#        vSlidesCandidates[idx2] = currSlide
#        vSlidesBestTags[idx2] = len(currSlide.tags)
#        vSlidesBestPairs[idx2] = idx1

vCandidates = getVCombi2(vPhotos)
print("here")
hSlidesCandidates = []
for photo in hPhotos:
    hSlidesCandidates.append(slide('H', [photo]))

hScores = [len(x.tags) for x in hSlidesCandidates]
vScores = [len(x.tags) for x in vCandidates]

slideshow = []

if len(hSlidesCandidates) > 0:
    maxHScore = max(hScores)
else:
    maxHScore = -1

if len(vCandidates) > 0:
    maxVScore = max(vScores)
else:
    maxVScore = -1

if maxHScore > maxVScore:
    popIdx = hScores.index(maxHScore)
    slideshow.append(hSlidesCandidates.pop(popIdx))
    hScores.pop(popIdx)
else:
    popIdx = vScores.index(maxVScore)
    
    slideshow.append(vCandidates.pop(popIdx))
    vScores.pop(popIdx)

while ((len(vCandidates) > 0) or (len(hSlidesCandidates) > 0)):
    
    print(len(vCandidates) + len(hSlidesCandidates))
    
    allCandidates = vCandidates + hSlidesCandidates
    allScores = vScores + hScores
    
    allScores = np.array(allScores)
    
    bestIdx = -1
    bestScore = -1
    
    for candidateIdx in allScores.argsort()[::-1]:
        currScore = calcTransScores(slideshow[-1], allCandidates[candidateIdx])
        
        if currScore > bestScore:
            bestScore = currScore
            bestIdx = candidateIdx
        
        if bestScore > allScores[candidateIdx] / 2:
            break
    
    slideshow.append(allCandidates[bestIdx])
    
    allScores = list(allScores)
    if slideshow[-1].slideType == 'H':
#        allScores.pop(bestIdx)
        hScores.pop(bestIdx - len(vCandidates))
#        allCandidates.pop(bestIdx)
        hSlidesCandidates.pop(bestIdx - len(vCandidates))
        
    elif slideshow[-1].slideType == 'V':
        
        vScores.pop(bestIdx)
        vCandidates.pop(bestIdx)

output_slideshow('./' + fname + '.txt', slideshow)


