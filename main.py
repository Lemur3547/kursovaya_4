import json

from src.classes import HeadHunterAPI, Vacancy

vacancies = HeadHunterAPI()
vacancies.get_vacancies('Python')

with open('data/vacancies.json', 'rt', encoding='utf-8') as file:
    vacancies = json.loads(file.read())

vac = vacancies['items'][0]
new_vac1 = Vacancy(vac['name'], vac['area']['name'], None, vac['address'], vac['employer'], vac['snippet'],
                   vac['contacts'], vac['schedule']['name'], vac['professional_roles'], vac['experience']['name'],
                   vac['alternate_url'])

new_vac2 = Vacancy(vac['name'], vac['area']['name'], 120000, vac['address'], vac['employer'], vac['snippet'],
                   vac['contacts'], vac['schedule']['name'], vac['professional_roles'], vac['experience']['name'],
                   vac['alternate_url'])
