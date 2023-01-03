# pdf convert to text /it does not work
"""from PyPDF4 import PdfFileReader
# begin of over-functon, definition
def pdf_convert():
    text_source =  open("../sources/text3.txt", "a+")
    def pdf_in_text_nested():
        # Open the PDF file in read-binary mode
            with open("../sources/Abstract_Olga_Dakischew-1.pdf","rb") as file: # 4.
                # Create a PDF object
                pdf = PdfFileReader(file) # 5.
                # Iterate over every page
                for page in range(pdf.getNumPages()): # 6.
                    # Extract the text from the page
                    return pdf.getPage(page).extractText() # 7.
                file.write(pdf_in_text_nested())
            # call the nested function
            text = pdf_in_text_nested()
            # write the thext in the file
            file.write(text)
# call the over-function
pdf_convert()
"""

# library's for extraction of text from pdf
# !pip install pdfminer.six
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
# convert the text to pdf
# !pip install fpdf
from fpdf import FPDF
#!pip install pdfkit
# import pdfkit (not implemented)
# convert text in pdf

with open('../docsources/text1.txt','r') as file:
    pdf = FPDF()
    pdf.add_page()
    text = file.read()
    pdf.set_xy(0, 0)
    pdf.set_font('Arial', '', 11)
    pdf.write(5,text)
    pdf.output('../docsources/text1.pdf', 'F')

# Coding
# extract-text-from-pdf function
def extract_text_from_pdf(docsources):

    output_string = StringIO()
    with open(docsources,'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return output_string.getvalue()

# open the file in write-mode
with open('../docsources/text2.txt', 'w+') as file:
    # call the extract-text-from-pdf function
    text = extract_text_from_pdf('../docsources/text2.pdf')
    # text write in the file
    file.write(text)

import chardet

with open('../docsources/corpus.txt', 'rb') as file:
    data = file.read()
    result = chardet.detect(data)
    corpus_text = data.decode(result['encoding'])
