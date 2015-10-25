# install:
# pip install PyPDF2

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def deletePage(inputPath,outputPath,index):
    output = PdfFileWriter()
    pdf = PdfFileReader(file(inputPath , "rb"))

    numOfPages = pdf.getNumPages()
    for i in range(0, numOfPages):
        if i != index:
            print i,index
            output.addPage(pdf.getPage(i))

    outputStream = file(outputPath, "wb")
    output.write(outputStream)
    outputStream.close()

def helpMsg():
    print "\n\
    usage: deletePdfPage.py [inputFile] [outputFile] [pageToDelete]\n\
    "

def main():
    if len(sys.argv)!=3:
        helpMsg()
        return

    inputPath = sys.argv[1]
    outputPath = sys.argv[2]
    index = int(sys.argv[3])
    deletePage(inputPath, outputPath,index)

if __name__ == '__main__':
    main()
