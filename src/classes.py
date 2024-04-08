import json
from abc import ABC, abstractmethod

import requests


class APIVacancies(ABC):
    @abstractmethod
    def get_vacancies(self, name):
        pass


class HeadHunterAPI(APIVacancies):
    def __init__(self):
        self.hh_api = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name):
        response = requests.get(self.hh_api, params={'text': name})
        vacancies = response.json()
        with open('data/vacancies.json', 'wt', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)
