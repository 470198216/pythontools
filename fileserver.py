from flask import Flask, request, jsonify
from flask import send_from_directory
import os
'''pip install flask requests'''
app = Flask(__name__)
UPLOAD_FOLDER = 'uploaded_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('C:\\Users\\wenjin\\Downloads', filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return jsonify({"message": f"File {file.filename} uploaded successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)