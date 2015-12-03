# install:
# pip install PyPDF2

import sys
import Image
from PyPDF2 import PdfFileMerger

TEMP_PDF = "TMP_IMAGE_PDF.pdf"

def addImageToPdf(pdfPath,imagePath,index):
    mergePdf = PdfFileMerger()

    img = Image.open(imagePath)
    img.save(TEMP_PDF, "PDF",resolution=100.0)

    mergePdf.append(file(pdfPath,'wb'))
    mergePdf.merge(index,file(TEMP_PDF,'wb'),"addedImg")

    outputStream = file("addedImg", "wb")
    mergePdf.write(outputStream)
    mergePdf.close()
    os.remove(TEMP_PDF)

def helpMsg():
    print "\n\
    usage: addImageToPdf.py [pdfFile] [imageFile] [pageToInsert]\n\
    "

def main():
    if len(sys.argv)!=4:
        helpMsg()
        return

    inputPath = sys.argv[1]
    outputPath = sys.argv[2]
    index = int(sys.argv[3])
    addImageToPdf(inputPath, outputPath,index)

if __name__ == '__main__':
    main()
