import tkinter as tk
from Button import Button
from PIL import ImageTk, Image
import os
from shutil import copy
from askDirectory import getFilePath, SetNewPath
from imageSize import fixImageSize
from subprocess import Popen

files = []
raw_files = []
currentImage = None
index = 0

root = tk.Tk()
root.title("image")
root.geometry("1100x900")

IMAGE_HEIGHT = 800
IMAGE_WIDTH = 800

panel = tk.Canvas(root, height=IMAGE_HEIGHT, width=IMAGE_WIDTH, bg='black')



def getDirList(path):
    global files, raw_files
    contentList = os.listdir(path)    

    for x in contentList:
        #print(x)
        if os.path.isfile(path+x):
            if x.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                files.append(path+x)
                raw_files.append(x)
            continue

        getDirList(path=path+x+'/')


def getImages(textfield):
    global files, raw_files
    files = list()
    raw_files = list()
    path = textfield.get(1.0, "end-1c")

    if os.path.exists(path):
        getDirList(path+'/')
        nextImage()
    else:
        textfield.delete(1.0, tk.END)
        textfield.insert(tk.END, "WRONG PATH")

def getPath(textfield):
    getFilePath(root, textfield)
    getImages(textfield)            

def nextImage():
    global index, files, panel, currentImage
    
    if not files:
        return

    index = index + 1
    
    if index >= len(files):
        index = 0

    #print(index)    

    currentImage = Image.open(files[index])
    newSize = fixImageSize(IMAGE_HEIGHT,IMAGE_WIDTH,(currentImage.height, currentImage.width))
    
    currentImage = ImageTk.PhotoImage(currentImage.resize(newSize))
    #panel.config(image=currentImage)
    panel.create_image(IMAGE_HEIGHT/2,IMAGE_WIDTH/2,image=currentImage)

def prevImage():
    global index, files, panel, currentImage
    
    if not files:
        return

    index = index - 1  
    
    if index < 0:
        index = len(files)-1

    #print(index)    
    currentImage = Image.open(files[index])
    newSize = fixImageSize(IMAGE_HEIGHT,IMAGE_WIDTH,(currentImage.height, currentImage.width))
    
    currentImage = ImageTk.PhotoImage(currentImage.resize(newSize))
    #panel.config(image=currentImage)
    panel.create_image(IMAGE_HEIGHT/2,IMAGE_WIDTH/2,image=currentImage)
    

newPath = ""      
def saveNewPath():
    global newPath
    newPath = SetNewPath(root)

def printNewPath():
    global newPath, files, index
    copy(files[index], newPath)

def openImageAsRegular():
    global files, index
    if files:
        sickPath = files[index].replace('/', '\\')

        Popen(fr'explorer /select, "{sickPath}"')





#print("FIRST : "+os.getcwd())
#getDirList(os.getcwd() + "/")


#print(files)
header = tk.Label(root)

button3 = tk.Button(header, text="بحث", command=lambda: getImages(textfield), width=10)
button4 = tk.Button(header, text="إختيار مجلد", command=lambda: getPath(textfield), width=10)

textfield = tk.Text(header, height=1)
textfield.pack(side=tk.RIGHT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)
header.pack(side=tk.TOP)
panel.pack()


if files:
    index = -1
    nextImage()


button = Button(root, text="التالي", command=nextImage)
button.pack(side=tk.RIGHT)

button2 = Button(root, text="رجوع", command=prevImage)

button2.pack(side=tk.LEFT)

footer = tk.Label(root)


button5 = Button(footer, text="إختيار مجلد النسخ", command=saveNewPath)
button6 = Button(footer, text="نسخ", command=printNewPath)
button7 = Button(footer, text="فتح موقع الصورة", command=openImageAsRegular)






button7.pack(side=tk.LEFT)
button5.pack(side=tk.LEFT)
button6.pack(side=tk.LEFT)
footer.pack(side=tk.BOTTOM)


root.mainloop()

