import requests
from API.yandex import token
href = 'https://cloud-api.yandex.net/v1/disk/resources'


def get_header():
    header = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}', 'Depth': '1'}
    return header

def create_folder(folder):
    params = {'path': folder}
    response = requests.put(href, headers= get_header(),params=params)
    return response

def get_info(folder):
    headers = get_header()
    params ={'path' : folder}
    resp = requests.get(href, headers=headers, params=params).json().get('type')
    return resp

def get_dir_list():
    # res = [item['name'] for item in get_info().json()['_embedded']['items'] if item['type']=='dir']
    ...
    # return res



if __name__ == '__main__':
    # print(create_folder('tests'))
    print(get_info('tests'))
    # print(get_dir_list())
