# Part 0: Reading Input File
with open(filename, 'r') as data:
    first_line = data.readline()
    params = first_line.split()
    num_videos = int(params[0])
    num_endpts = int(params[1])
    num_requests = int(params[2])
    num_caches = int(params[3])
    cache_size = int(params[4])
    cacheList = [Cache(x, cache_size) for x in range(num_caches)] # List of cache servers
    
    second_line = data.readline()
    video_sizes = [int(x) for x in second_line.split()]
    video_sizes = np.array(video_sizes)
    videoList = [Video(x, video_sizes[x]) for x in range(num_videos)] # List of videos
    
    dataCenterLatency = {}
    
    for i in range(num_endpts):
        endpoint_params = data.readline().split()
        dataCenterLatency[i] = int(endpoint_params[0])
        num_connections = int(endpoint_params[1]) # Number of caches connected to this endpoint
        for c in range(num_connections):
            connection_params = data.readline().split()
            cacheID = int(connection_params[0])
            latency = int(connection_params[1])
            cacheList[cacheID].update_latency(i, latency)
    
    for i in range(num_requests):
        request_params = data.readline().split()
        videoID = int(request_params[0])
        requesting_endpoint = int(request_params[1])
        num_requests = int(request_params[2])
        videoList[videoID].update_requests(requesting_endpoint, num_requests) # Update request details for video

totalCache = 0 # Store total cache capacity available
for cache in cacheList:
    totalCache += cache.capacity

# Part 1: 
# Store total number of latency saved for each video = number of requests * latency saved per request
videoSavings = [0] * num_videos

# Matrix (i, j) to store the latency saved by storing video i in cache j
videoSavingsPerCache = np.zeros((num_videos, num_caches))
