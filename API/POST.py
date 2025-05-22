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

    def execute(self, query: Query|str):
        payload = {'query': str(query)}
        r = requests.post(url=self.url, json=payload, headers=self.headers)

        return r.json()


class Mutation(POST):
    def execute(self, mutation: str):
        payload = {'query': mutation}
        r = requests.post(url=self.url, json=payload, headers=self.headers)

        return r.json()




