import pytest
import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'y0_AgAAAAAQY8qsAADLWwAAAADMqLooynTY04MrTd2a7yImlfkbpBXWMjI'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def test_createfolder():
    path = 'testAPI'
    result = requests.put(f'{URL}?path={path}', headers=headers)
    assert result.status_code == 200
