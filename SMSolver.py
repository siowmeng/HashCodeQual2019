#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 02:39:06 2019

@author: lowsiowmeng
"""

from classes import slide, calcTransScores, getVCombi
from parseInputSM import input_parser
from itertools import combinations
import numpy as np

hPhotos, vPhotos = input_parser('./Problem/c_memorable_moments.txt')
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

vSlidesCandidates, vSlidesBestTags, vSlidesBestPairs = getVCombi(vPhotos)

hSlidesCandidates = []
for photo in hPhotos:
    hSlidesCandidates.append(slide('H', [photo]))

hScores = [len(x.tags) for x in hSlidesCandidates]
#vScores = vSlidesBestTags

slideshow = []

if len(hSlidesCandidates) > 0:
    maxHScore = max(hScores)
else:
    maxHScore = -1

if len(vSlidesCandidates) > 0:
    maxVScore = max(vSlidesBestTags)
else:
    maxVScore = -1

if maxHScore > maxVScore:
    popIdx = hScores.index(maxHScore)
    slideshow.append(hSlidesCandidates.pop(popIdx))
    hScores.pop(popIdx)
else:
    popIdx = vSlidesBestTags.index(maxVScore)
    popIdxList = [popIdx, vSlidesBestPairs[popIdx]]
    
    slideshow.append(vSlidesCandidates.pop(max(popIdxList)))
    vSlidesCandidates.pop(min(popIdxList))
    
    vSlidesBestTags.pop(max(popIdxList))
    vSlidesBestTags.pop(min(popIdxList))
    
    vSlidesBestPairs.pop(max(popIdxList))
    vSlidesBestPairs.pop(min(popIdxList))
    
    vPhotos.pop(max(popIdxList))
    vPhotos.pop(min(popIdxList))

vSlidesCandidates, vSlidesBestTags, vSlidesBestPairs = getVCombi(vPhotos)

while ((len(vSlidesCandidates) > 0) or (len(hSlidesCandidates) > 0)):
    
    allCandidates = vSlidesCandidates + hSlidesCandidates
    allScores = vSlidesBestTags + hScores
    
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
        hScores.pop(bestIdx - len(vSlidesBestTags))
#        allCandidates.pop(bestIdx)
        hSlidesCandidates.pop(bestIdx - len(vSlidesBestTags))
        
    elif slideshow[-1].slideType == 'V':
        print("Best Index", bestIdx)
        print("Best Pair Index", vSlidesBestPairs[bestIdx])
        popIdxList = [bestIdx, vSlidesBestPairs[bestIdx]]
        
#        allScores.pop(max(popIdxList))
#        allScores.pop(min(popIdxList))
#        
#        allCandidates.pop(max(popIdxList))
#        allCandidates.pop(min(popIdxList))
#        
#        vSlidesBestPairs.pop(max(popIdxList))
#        vSlidesBestPairs.pop(min(popIdxList))
        
        vPhotos.pop(max(popIdxList))
        vPhotos.pop(min(popIdxList))
    
    #vSlidesBestPairs
    vSlidesCandidates, vSlidesBestTags, vSlidesBestPairs = getVCombi(vPhotos)
    


