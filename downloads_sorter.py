import os
import glob
import shutil
from os import path

filename = glob.glob("K:\Downloads\*") # downloads folder path

# file type endings arrays
text_documents = ['.pdf', '.docx', '.doc', '.txt','.log','.pgn']
images = ['.jpeg', '.jpg', '.svg', '.png', '.PNG','.ico','.webp','.emf','.jpg~','.png~','.kra','.gif','.ttf','.gbr','.abr','.jpeg~','.pur']
videos = ['.mp4', '.mp3','.mov','.MOV','.ogg']
setupFiles = ['.exe', '.msi', '.dmg','.deb','.dll','.bin']
compressedFiles = ['.zip', '.7zip','.jar','.rar','.gz','.ZIP']
codeFiles = ['.js','.css','.html','.json','.ahk','.py','.bat','.chm','.hs']
isoFiles = ['.iso']


#path of each sorted folder
isoFilesLocation = 'K:\Downloads_Sorted\Iso_Files'
DocumentsLocation = 'K:\Downloads_Sorted\Documents'
videosLocation = 'K:\Downloads_Sorted\Videos'
imagesLocation = 'K:\Downloads_Sorted\Images'
setupFilesLocation = 'K:\Downloads_Sorted\Setup_Files'
compressedFilesLocation = 'K:\Downloads_Sorted\Compressed_Files'
codeFilesLocation = 'K:\Downloads_Sorted\Code_Files'
otherFilesLocation = 'K:\Downloads_Sorted\Other'


for file in filename:
    # text_documents
    if os.path.splitext(file)[1] in text_documents:
        if (path.exists(DocumentsLocation)):
            shutil.move(file, DocumentsLocation)
        else:
            os.mkdir(DocumentsLocation)
            shutil.move(file, DocumentsLocation)
    
    # images
    elif os.path.splitext(file)[1] in images:
        if (path.exists(imagesLocation)):
            shutil.move(file, imagesLocation)
        else:
            os.mkdir(imagesLocation)
            shutil.move(file, imagesLocation)
            
    # videos
    elif os.path.splitext(file)[1] in videos:
        if (path.exists(videosLocation)):
            shutil.move(file, videosLocation)
        else:
            os.mkdir(videosLocation)
            shutil.move(file, videosLocation)
            
    # setup files
    elif os.path.splitext(file)[1] in setupFiles:
        if (path.exists(setupFilesLocation)):
            shutil.move(file, setupFilesLocation)
        else:
            os.mkdir(setupFilesLocation)
            shutil.move(file, setupFilesLocation)
            
    # compressed files
    elif os.path.splitext(file)[1] in compressedFiles:
        if (path.exists(compressedFilesLocation)):
            shutil.move(file, compressedFilesLocation)
        else:
            os.mkdir(compressedFilesLocation)
            shutil.move(file, compressedFilesLocation)
    
    # iso files
    elif os.path.splitext(file)[1] in isoFiles:
        if (path.exists(isoFilesLocation)):
            shutil.move(file, isoFilesLocation)
        else:
            os.mkdir(isoFilesLocation)
            shutil.move(file, isoFilesLocation)
    
    # code files
    elif os.path.splitext(file)[1] in codeFiles:
        if (path.exists(codeFilesLocation)):
            shutil.move(file, codeFilesLocation)
        else:
            os.mkdir(codeFilesLocation)
            shutil.move(file, codeFilesLocation)
    
    else:
        shutil.move(file, otherFilesLocation)
