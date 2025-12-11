import requests
from .Obj import Query
from pathlib import Path

class POST:
    url = 'https://api.monday.com/v2'

    def __init__(self):
        print(Path.cwd())
        with open('TOKEN', 'r') as file:
            key = file.read()

        self.headers = {"Authorization": key}

    def execute(self, query: Query|str) -> requests.Response:
        payload = {'query': str(query)}
        response = requests.post(url=self.url, json=payload, headers=self.headers)

        return response


class Mutation(POST):
    def execute(self, mutation: str) -> requests.Response:
        payload = {'query': mutation}
        response = requests.post(url=self.url, json=payload, headers=self.headers)

        return response




