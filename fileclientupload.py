import requests

def upload_file(file_path, url='http://172.29.132.153:5000/upload'):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
    print(response.json())

if __name__ == "__main__":
    file_path = 'C:\\Users\\wenjin\\Downloads\\mkinitramfs'  # 替换为你要上传的文件路径
    upload_file(file_path)