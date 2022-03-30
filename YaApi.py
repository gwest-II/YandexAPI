import requests

from pprint import pprint

TOKEN = 'AQAAAAAToWNoAADLW708z6vRzkXPiKhAKhqFMGc'
disk_url = 'https://cloud-api.yandex.net/v1/disk/resources'


class YaUpCreate:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, path: str):
        params = {'path': path}
        headers = self.get_headers()
        create_dir = requests.api.put(disk_url, headers=headers, params=params)
        return create_dir.status_code

    def delete_folder(self, path: str):
        params = {'path': path}
        headers = self.get_headers()
        delete_dir = requests.api.delete(disk_url, headers=headers, params=params)
        return delete_dir.status_code


if __name__ == '__main__':
    YaToken = YaUpCreate(token=TOKEN)

    pprint(YaToken.delete_folder('test'))
