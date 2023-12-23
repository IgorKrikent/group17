items_list = [('thing', 6.5), ('something', 60), ('aught', 100)]

processed_data = map(lambda i: str(i).strip("()").replace(',', ':'), items_list)

processed_items = list(processed_data)

random_list = [23, '15', 'Hello', 42.5, -107, '-22.5']

whole_numbers = filter(lambda s: str(s).lstrip('-').isdigit(), random_list)

with open('Whole_numbers_list.txt', mode='w', encoding='utf-8') as file:

    for number in whole_numbers:

        file.write(f'{number}\n')

