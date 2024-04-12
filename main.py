from src.classes import HeadHunterAPI, VacanciesFile
from src.presentation import presentation
from src.sort import convert_vacations_to_class, vacancies_sort


def interface():
    search = input("Введите запрос ")
    hh_api = HeadHunterAPI()
    hh_api.get_vacancies(search)

    while True:
        try:
            number_vacancies = int(input("Какое количество вакансий вывести "))
        except ValueError:
            print("Введите число вакансий")
        else:
            break

    tags = input("Введите ключевые слова для поиска ")
    vacancies_file = VacanciesFile()
    vacancies_list = vacancies_file.get_vacancy(tags)

    if not vacancies_list:
        print("Ничего не найдено")
        return

    vacancies_dict = convert_vacations_to_class(vacancies_list)
    sorted_vacancies = vacancies_sort(vacancies_dict)
    count = 0
    for vacancy in sorted_vacancies:
        if count < number_vacancies:
            presentation(vacancy)
            count += 1
        else:
            break


interface()
