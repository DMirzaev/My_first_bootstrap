import pandas as pd
from urllib.parse import urlencode
import requests
def download_yd(public_key_groups,separator):
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
    public_key = 'b93a44e7-b4b8-43ad-b490-db1721e98c08'
    final_url_groups = base_url + urlencode(dict(public_key=public_key_groups))  
    response_groups = requests.get(final_url_groups)  
    download_url_groups =  response_groups.json()['href']
    df = pd.read_csv(download_url_groups, sep=separator)
    return df