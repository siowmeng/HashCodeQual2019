from InputClass import photo
filepath = 'input/a_example.txt'
lines = open(filepath).readlines()
i = 0
photos = []
for line in lines:
    if i > 0:
        photo_info = line.split(' ')
        print(photo_info)
        orientation = photo_info[0]
        tag_num = int(photo_info[1])
        tags = []
        for j in range(tag_num):
            tags.append(photo_info[2+j].rstrip())
        photos.append(photo(orient=orientation,tags = tags))
    i += 1
