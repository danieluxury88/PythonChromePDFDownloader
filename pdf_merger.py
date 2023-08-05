import PyPDF2

def merge_pdfs(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged.pdf')
    

if __name__ == "__main__":
    pdf_list = ['file1.pdf', 'file2.pdf']
    merge_pdfs(pdf_list)
    print("PDFs have been merged.")