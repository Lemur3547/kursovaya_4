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


class Vacancy:
    def __init__(self, name, city, salary, address, employer, description, contacts, schedule, professional_roles,
                 experience, url):
        self.name = name
        self.city = city
        if self.salary is None:
            self.salary = 'Не указана'
        else:
            self.salary = salary
        self.address = address
        self.employer = employer
        self.description = description
        self.contacts = contacts
        self.schedule = schedule
        self.professional_roles = professional_roles
        self.experience = experience
        self.url = url

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, {self.city}, {self.salary}, {self.address}, {self.employer}, "
                f"{self.description}, {self.contacts}, {self.schedule}, {self.professional_roles}, {self.experience}, {self.url})")

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        return False

    def __gt__(self, other):
        if self.salary > other.salary:
            return True
        return False
