
import PyPDF2

MergePdf_Input = PyPDF2.PdfFileReader(open('Merged.pdf', 'rb'))         # add pdf to be watermarked
Wtr_Input = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))                 # add pdf from which to watermarked other pdf
Output = PyPDF2.PdfFileWriter()

# looping  through the pfd to be watermarked
for pdf in range(MergePdf_Input.getNumPages()):   
    pages = MergePdf_Input.getPage(pdf)
    pages.mergePage(Wtr_Input.getPage(0))            
    Output.addPage(pages)

    with open('WaterMarked.pdf', 'wb') as file:
        Output.write(file)



