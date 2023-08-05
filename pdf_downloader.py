import os
import requests
from bs4 import BeautifulSoup
import PyPDF2
from urllib.parse import urljoin

class PDFDownloader:
    
    def __init__(self, url) -> None:
        self.url = url
        self.download_folder = None
        self.pdf_links = None
        self.pdf_list = []
        
    def get_pdf_links(self):
        self.response = requests.get(self.url)
        if self.response.status_code != 200:
            print(F"Error: {self.response.status_code}")
            return
        soup = BeautifulSoup(self.response.content, 'html.parser')
        self.pdf_links = []
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href and href.endswith('.pdf'):
                self.pdf_links.append(urljoin(self.url, href))
                
        if not self.pdf_links:
            print("No PDF links found!")
        return  self.pdf_links
    
    def prepare_download_folder(self, folder_name):
        self.download_folder = folder_name
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        
    def download_pdfs(self, pdf_links, path):
        for pdf_link in pdf_links:
            filename = pdf_link.split('/')[-1]
            path = os.path.join(self.download_folder, filename)
            self.download_pdf(pdf_link, path)    
    
    def download_pdf(self, url, path):
        response = requests.get(url)
        if response.status_code != 200:
            print(F"Error: {response.status_code}")
        with open(path, 'wb') as f:
            f.write(response.content)
            filename = os.path.basename(path)
            self.pdf_list.append(filename)
            print(f"Downloaded {filename} at {path}")
        return filename
            # 
            
    def execute(self):
        self.get_pdf_links();
        self.prepare_download_folder('pdfs')
        self.download_pdfs(self.pdf_links, self.download_folder)
        self.merge_pdfs(self.pdf_list, self.download_folder)
        
    def merge_pdfs(self, pdf_list, download_folder):
        merger = PyPDF2.PdfMerger()
        for pdf in pdf_list:
            merger.append(pdf)
        output_filename = 'merged.pdf'
        output_path = os.path.join(download_folder, output_filename)
        merger.write(output_path)
            

        