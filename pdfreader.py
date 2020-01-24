import PyPDF2

pdfFile = open('sample.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(1)
print(pageObj.extractText())

pdfFile.close()
