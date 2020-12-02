import os
import glob
import shutil
from os import path

root = '/Users/kyle/downloads/'
destination = root

filename=glob.glob(root + "*")

documents = ['.docx', '.doc', '.txt', '.odt', '.csv', '.xlsx']
pdf = ['.pdf']
vectors = ['.ai', '.eps', '.svg']
images = ['.jpeg', '.jpg', '.png']
media = ['.mp3', '.mp4', '.wmv']

documentsDirectory = destination + 'documents'
pdfDirectory = destination + 'pdf'
vectorsDirectory = destination + 'vectors'
imagesDirectory = destination + 'images'
mediaDirectory = destination + 'media'

for file in filename:
    if os.path.splitext(file)[1] in documents:
        # Documents
        if(path.exists(documentsDirectory)):
            shutil.move(file,documentsDirectory)
        else:
            os.mkdir(documentsDirectory)
            shutil.move(file,documentsDirectory)
    if os.path.splitext(file)[1] in pdf:
        # PDFs
        if(path.exists(pdfDirectory)):
            shutil.move(file,pdfDirectory)
        else:
            os.mkdir(pdfDirectory)
            shutil.move(file,pdfDirectory)
    if os.path.splitext(file)[1] in vectors:
        # Vectors
        if(path.exists(vectorsDirectory)):
            shutil.move(file,vectorsDirectory)
        else:
            os.mkdir(vectorsDirectory)
            shutil.move(file,vectorsDirectory)
    if os.path.splitext(file)[1] in images:
        # Images
        if(path.exists(imagesDirectory)):
            shutil.move(file,imagesDirectory)
        else:
            os.mkdir(imagesDirectory)
            shutil.move(file,imagesDirectory)   
    if os.path.splitext(file)[1] in media:
        # Media
        if(path.exists(mediaDirectory)):
            shutil.move(file,mediaDirectory)
        else:
            os.mkdir(mediaDirectory)
            shutil.move(file,mediaDirectory)