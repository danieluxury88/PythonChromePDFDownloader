import unittest
from pdf_content_reader import PDFContentReader

class TestPDFContentReader(unittest.TestCase):
    def setUp(self):
        self.pdf = PDFContentReader('file1.pdf')
        
    def test_get_number_of_pages(self):
        self.assertEqual(self.pdf.get_number_of_pages(), 1)
        
    # def test_get_page(self):
    #     self.assertEqual(self.pdf.get_page(0), 'This is a test PDF file.')
        
    # def test_get_text(self):
    #     self.assertEqual(self.pdf.get_text(), 'This is a test PDF file.')