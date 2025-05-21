from PyPDF2 import PdfWriter
merger = PdfWriter()
n = int(input('We have 5 pdf how many you want to merge: '))
for i in range(0,n) :
    name = input(f'Enter the name of the  pdf {i + 1} : ')
    merger.append(name)

    merger.write('merged.pdf')
    merger.close()

'''
. GET SOME PDF'S AND USE THIS CODE TO MERGE PDF'S , IT CREATE A 'MERGER.PDF' DOCUMENT
# Pdf merger
. Using pypdf2 library to merger pdf files
. Import pdfwriter to create pdf documents
. Assing the pdfwriter in a variable merger and asks input from user that how many pdf need to merge.
. Usinf for loop in range of user input, ask user to enter the pdf name and append it to the merger variable using
write method and close merger.

'''   