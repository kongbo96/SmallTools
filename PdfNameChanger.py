import glob,os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

files = glob.glob(".//*.pdf")
for file in files:
    try:
        with open(file, 'rb') as fp:
            parser = PDFParser(fp)
            doc = PDFDocument(parser)
        title = doc.info[0]['Title'].decode('utf-8')
        title = title.replace(':', '：')
        print(title)
        os.rename(file, title + ".pdf")
    except:
        print(file)
    print()