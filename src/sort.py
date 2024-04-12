from src.classes import Vacancy


def convert_vacations_to_class(vacancies_list):
    class_vacancies_list = []
    for vacancy in vacancies_list:
        class_vacancies_list.append(
            Vacancy(vacancy['name'], vacancy['area']['name'], vacancy['salary'], vacancy['address'],
                    vacancy['employer'],
                    vacancy['snippet'], vacancy['contacts'], vacancy['schedule'], vacancy['professional_roles'],
                    vacancy['experience'], vacancy['alternate_url']))

    return class_vacancies_list


def vacancies_sort(vacancies_list):
    salary = []
    no_salary = []
    for vacancy in vacancies_list:
        if vacancy.salary != "Не указана" and vacancy.salary['from'] is not None:
            salary.append(vacancy)
        else:
            no_salary.append(vacancy)

    sorted_vacancies = sorted(salary, key=lambda x: x.salary['from'], reverse=True)
    sorted_vacancies.extend(no_salary)
    return sorted_vacancies
