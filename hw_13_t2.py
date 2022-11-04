import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type' : 'application/json',
            'Authorization' : f'OAuth {self.token}'
        }

    def upload(self, file_path : str, filename):
        """Method uploads file to yadisk"""
        href = self.get_upload_link(file_path)['href']

        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()

        if response.status_code == 201:
            print(f'Файл {filename} загружен')

    def get_upload_link(self, file_path):
        """Method gets upload URL"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path' : file_path, 'overwrite' : 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

if __name__ == '__main__':
    filename = 'uploadtest.txt'
    file_path = f'disk:/{filename}'
    token = 'x0x'
    uploader = YaUploader(token)
    uploader.upload(file_path, filename)