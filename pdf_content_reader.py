import PyPDF2

# convert to a class
class PDFContentReader:
    
    # create constructor
    # extract filename as attribute
    def __init__(self, pdf):
        self.file = pdf
        
    def read_pdf(self):
        with open(self.file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            number_of_pages = len(reader.pages)
            page = reader.pages[0]
            text = page.extract_text()
            print(text)
            
    def get_number_of_pages(self):
        with open(self.file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            number_of_pages = len(reader.pages)
            return number_of_pages
            
            
if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    reader = PDFContentReader(pdf_path)
    reader.read_pdf()