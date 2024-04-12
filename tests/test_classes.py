import json

import pytest

from src.classes import HeadHunterAPI, Vacancy, VacanciesFile


def test_head_hunter_api():
    hh_api = HeadHunterAPI()
    assert hh_api.get_vacancies("Python") is None


@pytest.fixture
def vacancy1():
    return Vacancy('Главный специалист', 'Санкт-Петербург',
                   {'from': 120000, 'to': None, 'currency': 'RUR'}, None, {'id': '104628', 'name': 'Газпром'}, {
                       'requirement': 'Навыки обработки, анализа и визуализации данных при помощи BI инструментов (Power BI, Apache Superset) или языков программирования (R и <highlighttext>Python</highlighttext>). – ',
                       'responsibility': 'Главный специалист (отдел коммерч-ой экспертизы управленческих решений по сбыту товарной продукции). – Проведение экспертизы и оценка экономического эффекта от заключения...'},
                   None, {'id': 'fullDay', 'name': 'Полный день'},
                   [{'id': '134', 'name': 'Финансовый аналитик, инвестиционный аналитик'}],
                   {'id': 'between3And6', 'name': 'От 3 до 6 лет'}, 'https://hh.ru/vacancy/96497148')


@pytest.fixture
def vacancy2():
    return Vacancy('Главный специалист', 'Санкт-Петербург',
                   None, None, {'id': '104628', 'name': 'Газпром'}, {
                       'requirement': 'Навыки обработки, анализа и визуализации данных при помощи BI инструментов (Power BI, Apache Superset) или языков программирования (R и <highlighttext>Python</highlighttext>). – ',
                       'responsibility': 'Главный специалист (отдел коммерч-ой экспертизы управленческих решений по сбыту товарной продукции). – Проведение экспертизы и оценка экономического эффекта от заключения...'},
                   None, {'id': 'fullDay', 'name': 'Полный день'},
                   [{'id': '134', 'name': 'Финансовый аналитик, инвестиционный аналитик'}],
                   {'id': 'between3And6', 'name': 'От 3 до 6 лет'}, 'https://hh.ru/vacancy/96497148')


def test_vacancy1(vacancy1):
    assert vacancy1.name == 'Главный специалист'
    assert vacancy1.city == 'Санкт-Петербург'
    assert vacancy1.salary == {'from': 120000, 'to': None, 'currency': 'RUR'}
    assert vacancy1.address is None
    assert vacancy1.employer == {'id': '104628', 'name': 'Газпром'}
    assert vacancy1.description == {
        'requirement': 'Навыки обработки, анализа и визуализации данных при помощи BI инструментов (Power BI, Apache Superset) или языков программирования (R и <highlighttext>Python</highlighttext>). – ',
        'responsibility': 'Главный специалист (отдел коммерч-ой экспертизы управленческих решений по сбыту товарной продукции). – Проведение экспертизы и оценка экономического эффекта от заключения...'}
    assert vacancy1.contacts is None
    assert vacancy1.schedule == {'id': 'fullDay', 'name': 'Полный день'}
    assert vacancy1.professional_roles == [{'id': '134', 'name': 'Финансовый аналитик, инвестиционный аналитик'}]
    assert vacancy1.experience == {'id': 'between3And6', 'name': 'От 3 до 6 лет'}
    assert vacancy1.url == 'https://hh.ru/vacancy/96497148'


def test_vacancy2(vacancy2):
    assert vacancy2.name == 'Главный специалист'
    assert vacancy2.city == 'Санкт-Петербург'
    assert vacancy2.salary == 'Не указана'
    assert vacancy2.address is None
    assert vacancy2.employer == {'id': '104628', 'name': 'Газпром'}
    assert vacancy2.description == {
        'requirement': 'Навыки обработки, анализа и визуализации данных при помощи BI инструментов (Power BI, Apache Superset) или языков программирования (R и <highlighttext>Python</highlighttext>). – ',
        'responsibility': 'Главный специалист (отдел коммерч-ой экспертизы управленческих решений по сбыту товарной продукции). – Проведение экспертизы и оценка экономического эффекта от заключения...'}
    assert vacancy2.contacts is None
    assert vacancy2.schedule == {'id': 'fullDay', 'name': 'Полный день'}
    assert vacancy2.professional_roles == [{'id': '134', 'name': 'Финансовый аналитик, инвестиционный аналитик'}]
    assert vacancy2.experience == {'id': 'between3And6', 'name': 'От 3 до 6 лет'}
    assert vacancy2.url == 'https://hh.ru/vacancy/96497148'


def test_comparison(vacancy1, vacancy2):
    vacancy1.salary = {'from': 120000, 'to': None, 'currency': 'RUR'}
    vacancy2.salary = {'from': 90000, 'to': None, 'currency': 'RUR'}
    assert vacancy1 > vacancy2
    assert not vacancy1 < vacancy2
    assert vacancy2 < vacancy1
    assert not vacancy2 > vacancy1
    vacancy1.salary = {'from': None, 'to': 100000, 'currency': 'RUR'}
    vacancy2.salary = {'from': None, 'to': 85000, 'currency': 'RUR'}
    assert not vacancy1 > vacancy2
    assert not vacancy1 < vacancy2
    vacancy1.salary = 'Не указана'
    vacancy2.salary = 'Не указана'
    assert not vacancy1 > vacancy2
    assert not vacancy1 < vacancy2


@pytest.fixture()
def vacancies_json():
    with open('test_data.json', 'wt', encoding='utf-8') as file:
        vacancies_list = [
            {'id': '96497148', 'premium': False, 'name': 'Главный специалист', 'department': None, 'has_test': False,
             'response_letter_required': False,
             'area': {'id': '2', 'name': 'Санкт-Петербург', 'url': 'https://api.hh.ru/areas/2'}, 'salary': None,
             'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
             'sort_point_distance': None, 'published_at': '2024-04-09T09:58:00+0300',
             'created_at': '2024-04-09T09:58:00+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=96497148',
             'show_logo_in_search': None, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/96497148?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/96497148', 'relations': [],
             'employer': {'id': '104628', 'name': 'Газпром', 'url': 'https://api.hh.ru/employers/104628',
                          'alternate_url': 'https://hh.ru/employer/104628',
                          'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/333051.jpeg',
                                        '240': 'https://img.hhcdn.ru/employer-logo/405908.jpeg',
                                        'original': 'https://img.hhcdn.ru/employer-logo-original/208765.JPG'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=104628',
                          'accredited_it_employer': False, 'trusted': True}, 'snippet': {
                'requirement': 'Навыки обработки, анализа и визуализации данных при помощи BI инструментов (Power BI, Apache Superset) или языков программирования (R и <highlighttext>Python</highlighttext>). – ',
                'responsibility': 'Главный специалист (отдел коммерч-ой экспертизы управленческих решений по сбыту товарной продукции). – Проведение экспертизы и оценка экономического эффекта от заключения...'},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '134', 'name': 'Финансовый аналитик, инвестиционный аналитик'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '94354526', 'premium': False, 'name': 'Стажер-разработчик Python', 'department': None,
             'has_test': False, 'response_letter_required': False,
             'area': {'id': '76', 'name': 'Ростов-на-Дону', 'url': 'https://api.hh.ru/areas/76'},
             'salary': {'from': 100000, 'to': 150000, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
             'sort_point_distance': None, 'published_at': '2024-04-08T10:52:47+0300',
             'created_at': '2024-04-08T10:52:47+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94354526',
             'show_logo_in_search': None, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/94354526?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/94354526', 'relations': [],
             'employer': {'id': '2071925', 'name': 'Додо Пицца', 'url': 'https://api.hh.ru/employers/2071925',
                          'alternate_url': 'https://hh.ru/employer/2071925',
                          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/524506.jpg',
                                        '240': 'https://img.hhcdn.ru/employer-logo/2539502.jpeg',
                                        '90': 'https://img.hhcdn.ru/employer-logo/2539501.jpeg'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=2071925',
                          'accredited_it_employer': False, 'trusted': True}, 'snippet': {
                'requirement': 'Мы ищем <highlighttext>Python</highlighttext>-разработчика, уровнем от Junior и выше, желательно с опытом развития новых продуктов. Уверенные знания <highlighttext>Python</highlighttext> 3.8...',
                'responsibility': 'Разработка небольших проектов. Проектная работа.'}, 'contacts': None,
             'schedule': {'id': 'fullDay', 'name': 'Полный день'},
             'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None}]
        json.dump(vacancies_list, file, ensure_ascii=False)


def test_add_vacancy(vacancies_json):
    vacancies_file = VacanciesFile('test_data.json')
    vacancies_file.add_vacancy(
        {'id': '96354500', 'premium': False, 'name': 'Программист', 'department': None, 'has_test': False,
         'response_letter_required': False,
         'area': {'id': '159', 'name': 'Астана', 'url': 'https://api.hh.ru/areas/159'},
         'salary': None, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
         'sort_point_distance': None, 'published_at': '2024-04-07T17:33:30+0300',
         'created_at': '2024-04-07T17:33:30+0300',
         'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=96354500',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/96354500?host=hh.ru',
         'alternate_url': 'https://hh.ru/vacancy/96354500', 'relations': [],
         'employer': {'id': '10428882', 'name': 'DISYS', 'url': 'https://api.hh.ru/employers/10428882',
                      'alternate_url': 'https://hh.ru/employer/10428882',
                      'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1201355.png',
                                    '240': 'https://img.hhcdn.ru/employer-logo/6425870.png',
                                    '90': 'https://img.hhcdn.ru/employer-logo/6425869.png'},
                      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10428882',
                      'accredited_it_employer': False,
                      'trusted': True}, 'snippet': {'requirement': 'Можно без опыта.',
                                                    'responsibility': 'Разработка небольших проектов. Проектная работа.'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [
             {'id': 'from_four_to_six_hours_in_a_day', 'name': 'Можно работать сменами по\xa04–6 часов в\xa0день'}],
         'working_time_modes': [], 'accept_temporary': True,
         'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
         'employment': {'id': 'part', 'name': 'Частичная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None})

    with open('test_data.json', 'rt', encoding='utf-8') as file:
        vacancies_list = json.load(file)

    assert vacancies_list[0]['id'] == '96497148'
    assert vacancies_list[1]['id'] == '94354526'
    assert vacancies_list[2]['id'] == '96354500'


def test_get_vacancy(vacancies_json):
    vacancies_file = VacanciesFile('test_data.json')

    suitable_vacancies = vacancies_file.get_vacancy('')
    assert len(suitable_vacancies) == 2
    assert suitable_vacancies[0]['id'] == '96497148'
    assert suitable_vacancies[1]['id'] == '94354526'


def test_get_vacancy_name(vacancies_json):
    vacancies_file = VacanciesFile('test_data.json')

    suitable_vacancies = vacancies_file.get_vacancy('специалист, разработчик')
    assert len(suitable_vacancies) == 2
    assert suitable_vacancies[0]['id'] == '96497148'
    assert suitable_vacancies[1]['id'] == '94354526'


def test_get_vacancy_requirement(vacancies_json):
    vacancies_file = VacanciesFile('test_data.json')

    suitable_vacancies = vacancies_file.get_vacancy('анализ, Junior')
    assert len(suitable_vacancies) == 2
    assert suitable_vacancies[0]['id'] == '96497148'
    assert suitable_vacancies[1]['id'] == '94354526'


def test_get_vacancy_responsibility(vacancies_json):
    vacancies_file = VacanciesFile('test_data.json')

    suitable_vacancies = vacancies_file.get_vacancy('эффект, проект')
    assert len(suitable_vacancies) == 2
    assert suitable_vacancies[0]['id'] == '96497148'
    assert suitable_vacancies[1]['id'] == '94354526'


def test_get_vacancy_professional_roles(vacancies_json):
    vacancies_file = VacanciesFile('test_data.json')

    suitable_vacancies = vacancies_file.get_vacancy('аналитик, разработчик')
    assert len(suitable_vacancies) == 2
    assert suitable_vacancies[0]['id'] == '96497148'
    assert suitable_vacancies[1]['id'] == '94354526'


def test_del_vacancy(vacancies_json):
    vacancies_file = VacanciesFile('test_data.json')
    vacancies_file.del_vacancy(96497148)
    with open('test_data.json', 'rt', encoding='utf-8') as file:
        vacancies_list = json.load(file)

    assert len(vacancies_list) == 1
    assert vacancies_list[0]['id'] == '94354526'
