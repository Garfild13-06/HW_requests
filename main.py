import requests
from pprint import pprint
import datetime as dt


def task_1(heroes_list):
    my_url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(my_url)
    data = response.json()
    intelligence_dict = {}
    for rec in data:
        if rec["name"] in (heroes_list):
            intelligence_dict[rec["powerstats"]["intelligence"]] = rec["name"]
    intelligence_list = sorted(intelligence_dict.keys(), reverse=True)
    print(f"{intelligence_dict[intelligence_list[0]]} является самым умным супергероем")


class YaUploader:

    def __init__(self, token):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, file_path: str):
        href = self._get_upload_link(disk_file_path=file_path).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        return response.status_code


def task_2(token):
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(file_path="test.txt")
    pprint(result)


def task_3():
    timestamp = dt.datetime.now()
    to_date = int(dt.datetime.timestamp(timestamp))
    from_date = to_date - 172800
    url = "https://api.stackexchange.com/2.3/answers"
    params = {"fromdate": from_date, "todate": to_date, "order": "desc", "sort": "activity", "tagged": "python",
              "filter": "default", "site": "stackoverflow"}
    response = requests.get(url=url, params=params)
    result = response.text
    return result


task_1(["Hulk", "Captain America", "Thanos"])
# task_2("")
pprint(task_3())
