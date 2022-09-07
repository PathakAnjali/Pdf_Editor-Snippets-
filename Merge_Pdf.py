import PyPDF2
import sys

input_pdf = sys.argv[1:]

def pdfMerger(n):
    merger = PyPDF2.PdfFileMerger()  # method to merge the pdf

    for pdf in n:
        print(pdf)
        merger.append(pdf)
    merger.write('Merged.pdf')

pdfMerger(input_pdf)
