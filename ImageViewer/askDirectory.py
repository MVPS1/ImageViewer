import tkinter as tk
from tkinter import filedialog
import os




def getFilePath(root, textfield):
    currentDir = os.getcwd()
    tempDir = filedialog.askdirectory(parent=root, initialdir=currentDir, title='file here')

    #if len(tempDir):
        #print("THIS IS YOUR DIRECTORY : ", tempDir)
    textfield.delete(1.0, tk.END)
    textfield.insert(tk.END, tempDir)

def SetNewPath(root):
    currentDir = os.getcwd()
    tempDir = filedialog.askdirectory(parent=root, initialdir=currentDir, title='file here')

    #if len(tempDir):
        #print("THIS IS YOUR DIRECTORY : ", tempDir)
    return tempDir








