students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

# Чтоб не подчеркивало
new_student = {
     'Пошта': 'M_K2009@gmail.com',
     'Вік': 27,
     'Номер телефону': '+380987893006',
     'Середній бал': 99.9
}

students['Михайло Коваль'] = new_student

total_mark = 0.0

for value in students.values():

    total_mark += value['Середній бал']

group_gpa = round(total_mark / len(students), 1)

print(f'{group_gpa=}')

students['Іван Петров']['bank_account_number'] = None

zhenya_salary = students['Женя Курич'].get('Зарплатня') or 0

print(f'{zhenya_salary=}')

