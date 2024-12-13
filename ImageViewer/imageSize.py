from PIL import ImageTk, Image



def fixImageSize(height, width, image):
    newHeight = image[0]
    newWidth = image[1]
    
    if image[0] > image[1]:
        if image[0] > height:
            newWidth = image[1] * (height / image[0])
            newHeight = height
    elif image[1] > width:
        newHeight = image[0] * (width / image[1])
        newWidth = width
                
    #print((int(newWidth), int(newHeight)))
    return(int(newWidth), int(newHeight))
            
