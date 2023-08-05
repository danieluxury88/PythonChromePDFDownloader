from flask import Flask, request, jsonify
from flask_cors import CORS
import pdf_downloader

app = Flask(__name__)
CORS(app)

@app.route('/get_url', methods=['POST'])
def get_url():
    data = request.get_json()
    print("Received URL: ", data['url'])
    pdfDownloader = pdf_downloader.PDFDownloader(data['url'])
    pdfDownloader.execute()
    return jsonify({'message': 'Success'}), 200


if __name__ == '__main__':
    app.run(port=5001)
