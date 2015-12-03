
from PyPDF2 import PdfFileReader, PdfFileWriter

def addPdf(inputPath, addPath, outputPath):

    inputPdf = PdfFileReader(open(inputPath , "rb"))
    addPdf = PdfFileReader(open(addPath , "rb"))

    numOfInputPages = inputPdf.getNumPages()
    numOfAddPages = addPdf.getNumPages()

    outputWriter = PdfFileWriter()

    for i in range(0, numOfInputPages):
        outputWriter.addPage(inputPdf.getPage(i))
    for i in range(0, numOfAddPages):
        outputWriter.addPage(addPdf.getPage(i))

    def writePdf2File(writer,path):
    	stream = open(path, "wb")
    	writer.write(stream)
    	stream.close()

    writePdf2File(outputWriter,outputPath)

addPdf("test.pdf","tmp.pdf","out.pdf")
