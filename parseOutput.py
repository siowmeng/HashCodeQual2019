# Part 3: Write results to output file
noCacheServers = sum(np.sum(finalResults, axis = 1) > 0) # Number of cache servers used
with open(filename.split('.')[0] + '.out', 'w') as fd:
    fd.write(str(noCacheServers) + '\n')
    for i in range(num_caches):
        if sum(finalResults[i]) > 0:   
            writeLine = str(i)
        for vidCache in np.where(finalResults[i])[0]:
            writeLine += (' ' + str(vidCache))
        fd.write(writeLine + '\n')
