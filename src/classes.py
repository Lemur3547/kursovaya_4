import json
import re
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
            json.dump(vacancies['items'], file, ensure_ascii=False)


class Vacancy:
    def __init__(self, name, city, salary, address, employer, description, contacts, schedule, professional_roles,
                 experience, url):
        self.name = name
        self.city = city
        if salary is None:
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
                f"{self.description}, {self.contacts}, {self.schedule}, {self.professional_roles}, {self.experience}, "
                f"{self.url})")

    def __lt__(self, other):
        if self.salary != 'Не указана' and other.salary != 'Не указана':
            if self.salary["from"] is not None and other.salary["from"] is not None:
                if self.salary['from'] < other.salary['from']:
                    return True
                return False
            return False
        return False

    def __gt__(self, other):
        if self.salary != 'Не указана' and other.salary != 'Не указана':
            if self.salary["from"] is not None and other.salary["from"] is not None:
                if self.salary['from'] > other.salary['from']:
                    return True
                return False
            return False
        return False


class VacanciesActions(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy(self, tags):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy_id):
        pass


class VacanciesFile(VacanciesActions):

    def __init__(self, directory='data/vacancies.json'):
        self.directory = directory

    def add_vacancy(self, new_vacancy):
        with open(self.directory, 'rt', encoding='utf-8') as file:
            vacancies_list = json.load(file)
        with open(self.directory, 'wt', encoding='utf-8') as file:
            vacancies_list.append(new_vacancy)
            json.dump(vacancies_list, file, ensure_ascii=False)

    def get_vacancy(self, tags):
        tags = re.sub(r"[,:;.!?]", "", tags)
        tags_list = tags.split()
        with open(self.directory, 'rt', encoding='utf-8') as file:
            vacancies = json.load(file)
            if tags_list:
                suitable_vacancies = []
                for vacancy in vacancies:
                    for tag in tags_list:
                        if tag.lower() in vacancy['name'].lower():
                            if vacancy not in suitable_vacancies:
                                suitable_vacancies.append(vacancy)
                        if vacancy["snippet"]["requirement"] is not None:
                            if tag.lower() in vacancy["snippet"]["requirement"].lower():
                                if vacancy not in suitable_vacancies:
                                    suitable_vacancies.append(vacancy)
                        if vacancy["snippet"]["responsibility"] is not None:
                            if tag.lower() in vacancy["snippet"]["responsibility"].lower():
                                if vacancy not in suitable_vacancies:
                                    suitable_vacancies.append(vacancy)
                        if tag.lower() in vacancy["professional_roles"][0]["name"].lower():
                            if vacancy not in suitable_vacancies:
                                suitable_vacancies.append(vacancy)
                return suitable_vacancies
            return vacancies

    def del_vacancy(self, vacancy_id):
        with open(self.directory, 'rt', encoding='utf-8') as file:
            vacancies = json.load(file)
        with open(self.directory, 'wt', encoding='utf-8') as file:
            for vacancy in vacancies:
                if str(vacancy_id) == vacancy['id']:
                    vacancies.remove(vacancy)
            json.dump(vacancies, file, ensure_ascii=False)
