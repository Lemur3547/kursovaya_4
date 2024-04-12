import pytest

from src.classes import Vacancy
from src.presentation import presentation


@pytest.fixture
def vacancy():
    return Vacancy('Главный специалист', 'Санкт-Петербург',
                   {'from': 120000, 'to': None, 'currency': 'RUR'}, None, {'id': '104628', 'name': 'Газпром'}, {
                       'requirement': 'Навыки обработки, анализа и визуализации данных при помощи BI инструментов (Power BI, Apache Superset) или языков программирования (R и <highlighttext>Python</highlighttext>). – ',
                       'responsibility': 'Главный специалист (отдел коммерч-ой экспертизы управленческих решений по сбыту товарной продукции). – Проведение экспертизы и оценка экономического эффекта от заключения...'},
                   None, {'id': 'fullDay', 'name': 'Полный день'},
                   [{'id': '134', 'name': 'Финансовый аналитик, инвестиционный аналитик'}],
                   {'id': 'between3And6', 'name': 'От 3 до 6 лет'}, 'https://hh.ru/vacancy/96497148')


def test_presentation(vacancy):
    assert presentation(vacancy) is None

    vacancy.salary = "Не указана"
    vacancy.address = {'raw': 'Минск, проспект Дзержинского, 3Б'}
    vacancy.contacts = '+7(904)234-53-56'
    assert presentation(vacancy) is None

    vacancy.salary = {'from': 120000, 'to': 140000, 'currency': 'RUR'}
    assert presentation(vacancy) is None

    vacancy.salary = {'from': None, 'to': 120000, 'currency': 'RUR'}
    assert presentation(vacancy) is None
