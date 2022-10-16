import requests

class ydisk():
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    TOKEN = 'y0_AgAAAAAQY8qsAADLWwAAAADMqLooynTY04MrTd2a7yImlfkbpBXWMjI'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

    def test_createfolder(self):
        path = 'testAPI'
        result = requests.put(f'{self.URL}?path={path}', headers=self.headers)
        return result.status_code

yd = ydisk()
print(yd.test_createfolder())