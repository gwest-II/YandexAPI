import requests

from pprint import pprint

TOKEN = ''


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(file_url, headers=headers)
        return response.json()

    def _upload(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true', 'fields': 'name'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._upload(disk_file_path=disk_file_path).get('href', filename)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.raise_for_status() == 201:
            print('Success')


if __name__ == '__main__':
    file_list = YaUploader(token=TOKEN)
    # pprint(file_list.get_files_list())
    pprint(file_list.upload_file_to_disk('test_path/text30.txt', text30.txt))
