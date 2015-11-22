
from PyPDF2 import PdfFileReader, PdfFileWriter

def splitPdf(inputPath, splitLeftPath,splitRightPath,splitIndex):

    pdf = PdfFileReader(open(inputPath , "rb"))

    numOfPages = pdf.getNumPages()
    if splitIndex<0:
    	print("split index should be native number. task canceled!")
    	return
    if numOfPages<=splitIndex:
    	print("split index is out of page range. task canceled!")
    	return

    leftWriter = PdfFileWriter()
    rightWriter = PdfFileWriter()

    for i in range(0, numOfPages):
        if i<splitIndex:
            leftWriter.addPage(pdf.getPage(i))
        else:
        	rightWriter.addPage(pdf.getPage(i))

    def writePdf2File(writer,path):
    	stream = open(path, "wb")
    	writer.write(stream)
    	stream.close()

    writePdf2File(leftWriter,splitLeftPath)
    writePdf2File(rightWriter,splitRightPath)

splitPdf("1.pdf","left.pdf","right.pdf",4)
