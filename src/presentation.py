def presentation(vacancy):
    print(vacancy.name)

    if vacancy.salary != "Не указана":
        if vacancy.salary['from'] is not None and vacancy.salary['to'] is not None:
            print(f"Зарплата: {vacancy.salary['from']} - {vacancy.salary['to']} {vacancy.salary['currency']}")
        elif vacancy.salary['from'] is not None:
            print(f"Зарплата: от {vacancy.salary['from']} {vacancy.salary['currency']}")
        elif vacancy.salary['to'] is not None:
            print(f"Зарплата: до {vacancy.salary['to']} {vacancy.salary['currency']}")
    else:
        print(f"Зарплата: {vacancy.salary}")

    print()

    print(vacancy.employer['name'])

    if vacancy.address is not None:
        print(vacancy.address['raw'])
    else:
        print(vacancy.city)

    print()

    print(f'Требуемый опыт: {vacancy.experience["name"]}')
    print(f'Занятость: {vacancy.schedule['name']}\n')

    if vacancy.description['requirement'] is not None:
        print(vacancy.description['requirement'])
    if vacancy.description['responsibility'] is not None:
        print(vacancy.description['responsibility'])

    print()

    print(f'Требуемые навыки: {vacancy.professional_roles[0]['name']}\n')
    if vacancy.contacts is not None:
        print(f"Контактные данные: {vacancy.contacts}")
    else:
        print(f"Контактные данные: не указаны")

    print(f"Ссылка на вакансию: {vacancy.url}")
    print("\n\n")
