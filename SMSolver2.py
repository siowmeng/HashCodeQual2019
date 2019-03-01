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

hPhotos, vPhotos = input_parser('./Problem/' + fname + '.txt')

vCandidates = getVCombi2(vPhotos)

hCandidates = []
for photo in hPhotos:
    hCandidates.append(slide('H', [photo]))

hScores = [len(x.tags) for x in hCandidates]
vScores = [len(x.tags) for x in vCandidates]

slideshow = []

#print("H Candidates Bef:")
#for hCand in hCandidates:
#    print([x.photoID for x in hCand.photos])
#print("V Candidates Bef:")
#for vCand in vCandidates:
#    print([x.photoID for x in vCand.photos])

if len(hCandidates) > 0:
    minHScore = min(hScores)
else:
    minHScore = -1
    
if len(vCandidates) > 0:
    minVScore = min(vScores)
else:
    minVScore = -1

if (minVScore == -1) or (minVScore < minHScore):
    popIdx = hScores.index(minHScore)
    slideshow.append(hCandidates.pop(popIdx))
    hScores.pop(popIdx)
else:
    popIdx = vScores.index(minVScore)    
    slideshow.append(vCandidates.pop(popIdx))
    vScores.pop(popIdx)

#if (minHScore < minVScore) and (minHScore != -1):
#    popIdx = hScores.index(minHScore)
#    slideshow.append(hCandidates.pop(popIdx))
#    hScores.pop(popIdx)
#elif (minVScore < minHScore) and (minVScore != -1):
#    popIdx = vScores.index(minVScore)    
#    slideshow.append(vCandidates.pop(popIdx))
#    vScores.pop(popIdx)

#print("H Candidates Aft:")
#for hCand in hCandidates:
#    print([x.photoID for x in hCand.photos])
#print("V Candidates Aft:")
#for vCand in vCandidates:
#    print([x.photoID for x in vCand.photos])

allCandidates = vCandidates + hCandidates
allScores = vScores + hScores

#while ((len(vCandidates) > 0) or (len(hCandidates) > 0)):
while (len(allCandidates) > 0):
    
#    print("Slideshow")
#    for slideIter in slideshow:
#        print([x.photoID for x in slideIter.photos])
    
    print(len(allCandidates))
#    print("All candidates")
#    for candidate in allCandidates:
#        print([x.photoID for x in candidate.photos])
    
    allScores = np.array(allScores)
    
    bestIdx = -1
    bestScore = -1
    
    searchTagsLength = len(slideshow[-1].tags)
    #for candidateIdx in allScores.argsort()[::-1]:
    for candidateIdx in allScores.argsort():
        
        #if bestScore > allScores[candidateIdx] / 2:
        if (allScores[candidateIdx] > searchTagsLength):
            
            if bestScore > -1:
                break
            else:
                searchTagsLength = allScores[candidateIdx]
        
        currScore = calcTransScores(slideshow[-1], allCandidates[candidateIdx])
        
        if currScore > bestScore:
            bestScore = currScore
            bestIdx = candidateIdx
    
    slideshow.append(allCandidates.pop(bestIdx))
    
    allScores = list(allScores)
    allScores.pop(bestIdx)
    
output_slideshow('./' + fname + '_solution.txt', slideshow)
print("Final Score: " + str(calcSlideshowScores(slideshow)))

