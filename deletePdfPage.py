# Merge two PDFs
from PyPDF2 import PdfFileReader, PdfFileWriter

def deletePage(inputPath, outputPath,index):
    output = PdfFileWriter()
    pdf = PdfFileReader(file(inputPath , "rb"))

    numOfPages = pdf.getNumPages()
    for i in range(0, numOfPages):
        if i != index:
            output.addPage(pdf.getPage(i))

    outputStream = file(outputPath, "wb")
    output.write(outputStream)
    outputStream.close()

deletePage("output.pdf","tmp.pdf",0)
