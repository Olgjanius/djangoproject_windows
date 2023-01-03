# librarys for extraction of text from pdf
# !pip install pdfminer.six
from io import StringIO

import nltk
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

# definiton of extract-text-from-pdf function
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

# librarys for frame, lower() function
# !pip install pandas
import pandas as pd

# convert text in frame
with open('../docsources/text1.txt', 'r') as file:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    dataframe = pd.DataFrame(file)
    print(dataframe)
    string_dataframe = str(dataframe)
    lower_dataframe = string_dataframe.lower()
    print("lower_dataframe: " + lower_dataframe)
    # https://docs.python.org/3/library/re.html
    #dataframe = dataframe.str.replace('[^\w\s]', "")
    #print("dataframe_cleaned: " + dataframe)
# !pip install wordcloud
# !pip install matplotlib
# !pip install HanTa
from HanTa import HanoverTagger as ht
import matplotlib.pyplot as plt
import pandas as pd
from nltk.stem.snowball import SnowballStemmer, GermanStemmer
from nltk import PorterStemmer, LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import string
with open('../docsources/text3.txt', 'w+') as file:
    # dataframe wird nicht in file geschrieben:
    file.write("Dataframe as string:" + string_dataframe)
    file.write("Dataframe as string in lowercase:" + lower_dataframe)
    #file.write("Dataframe as string in lowercase cleaned:" + dataframe)
# Coding
# !pip install nltk
import re
with open('../docsources/text4.txt', 'r') as file:
    file_in_token = text
    #tokenize with re
    file_tokenized = nltk.word_tokenize(file_in_token)
    " | ".join(file_tokenized)
    print(file_tokenized)

with open('../docsources/text4.txt', 'w+') as file:

    # nltk.word_tokenized wird nicht in file geschrieben:
    file.write(str(file_tokenized))


