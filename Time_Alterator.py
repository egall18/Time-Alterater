import math
import glob
from PIL import Image

def getData(pic): #function
    new_image = []
    newList = []
    R = []
    G = []
    B = []
    for p in pic: #append the data (tuples) inside newList
        newList.append(list(p.getdata()))

    middle = len(newList)//2 #find the median

    for i in range(len(newList[0])): #goes through each pixel (1.4 million)
        for j in range(len(newList)): #goes through each image
            R.append(newList[j][i][0]) #stores each red tuple into R list
            G.append(newList[j][i][1]) #stores each green tuple into R list
            B.append(newList[j][i][2]) #stores each blue tuple into R list
        R.sort() #sorts every red in ascending order
        G.sort() #sorts every green in ascending order
        B.sort() #sorts every blue in ascending order
        new_image.append((R[middle], G[middle], B[middle])) #set R, G, B medians into new image
        R.clear()
        G.clear()
        B.clear()
    return new_image

path = glob.glob("/Users/batman/desktop/images/*.png") # This will get all files from the images directory
ls = []
for pic in path:  # We store the open images into ls list
    ls.append(Image.open(pic))

new_image = getData(ls)
canvas = Image.new('RGB', ls[0].size)  
canvas.putdata(new_image)
canvas.save("clean_image.png")
canvas.show()



