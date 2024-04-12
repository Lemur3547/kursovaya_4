import json

import pytest

from src.classes import Vacancy
from src.sort import convert_vacations_to_class, vacancies_sort


@pytest.fixture
def vacancies_list():
    return [{'name': 'Главный специалист',
             'area': {'id': '2', 'name': 'Санкт-Петербург', 'url': 'https://api.hh.ru/areas/2'}, 'salary': {'from': 120000, 'to': None, 'currency': 'RUR'},
             'address': None, 'alternate_url': 'https://hh.ru/vacancy/96497148',
             'employer': {'id': '104628', 'name': 'Газпром'}, 'snippet': {
            'requirement': 'Навыки обработки, анализа и визуализации данных при помощи BI инструментов (Power BI, Apache Superset) или языков программирования (R и <highlighttext>Python</highlighttext>). – ',
            'responsibility': 'Главный специалист (отдел коммерч-ой экспертизы управленческих решений по сбыту товарной продукции). – Проведение экспертизы и оценка экономического эффекта от заключения...'},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'},
             'professional_roles': [{'id': '134', 'name': 'Финансовый аналитик, инвестиционный аналитик'}],
             'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'}
             }, {
                'name': 'Web-программист - стажер',
                'area': {'id': '160', 'name': 'Алматы', 'url': 'https://api.hh.ru/areas/160'}, 'salary': {'from': None, 'to': 100000, 'currency': 'RUR'},
                'address': None, 'alternate_url': 'https://hh.ru/vacancy/96507348',
                'employer': {'id': '5031522', 'name': 'Autodata'}, 'snippet': {
            'requirement': 'Знать теорию тестирования, что такое тест планы, чек листы и протокол тестирования, свободно владеть ЯП <highlighttext>Python</highlighttext>, быть приспособленным к монотонной...',
            'responsibility': 'Как правильно работать с git-ом в команде. Писать автотесты на базе Selenium/<highlighttext>Python</highlighttext> (тестировщик). Создавать web-дизайны для реальных...'},
                'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'},
                'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                'experience': {'id': 'noExperience', 'name': 'Нет опыта'}
            }]


def test_convert_vacations_to_class(vacancies_list):
    class_vacancies = convert_vacations_to_class(vacancies_list)
    assert print(class_vacancies) is None

    class_vacancies_list = vacancies_sort(class_vacancies)
    assert class_vacancies_list[0].salary == {'from': 120000, 'to': None, 'currency': 'RUR'}
    assert class_vacancies_list[1].salary == {'from': None, 'to': 100000, 'currency': 'RUR'}



