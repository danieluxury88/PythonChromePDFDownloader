from reportlab.pdfgen import canvas

def create_pdf(file_path, text):
    c = canvas.Canvas(file_path)
    c.drawString(100, 700, text)
    c.save()

if __name__ == "__main__":
    filename = input("Enter the name of the PDF file: ")
    user_input = input("Enter the text you want to include in the PDF: ")
    
    create_pdf(filename, user_input)
    print(f"PDF file '{filename}' with the text '{user_input}' has been created.")
