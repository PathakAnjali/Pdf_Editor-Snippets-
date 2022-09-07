
import PyPDF2

MergePdf_Input = PyPDF2.PdfFileReader(open('Merged.pdf', 'rb'))
Wtr_Input = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
Output = PyPDF2.PdfFileWriter()

# looping  through the pfd to be watermarked
for pdf in range(MergePdf_Input.getNumPages()):     # unaware of the no. of pgs in pdf so using getNumPages
    pages = MergePdf_Input.getPage(pdf)
    pages.mergePage(Wtr_Input.getPage(0))             # as Wtr_Input have only one page, merging wtr mark pdf on all the pages
    Output.addPage(pages)

    with open('WaterMarked.pdf', 'wb') as file:
        Output.write(file)



