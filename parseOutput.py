def output_slideshow(filename, slide_list):
    """
    returns: Output File given a list of slide class
    """
    """Writes an output file with the required format."""
    with open(filename, 'w') as f:

        f.write(f"{len(slide_list)}\n")

        for slide in slide_list:
            if slide.slideType == 'V':
                V1, V2 = slide.photos
                f.write(f"{V1.photoID} {V2.photoID}\n")
            else:
                H = slide.photos[0]
                f.write(f"{H.photoID}\n")