import requests

import sys

my_url = ('https://script.google.com/macros/s/AKfycbx'
          'l4r9LA5XUA60lZRP5YRLNbOb7ZwAT2ZkvTIMrQMn3U'
          'lvFTb_5CuFB3GQoFXBzei1o/exec')

response = requests.get(url=my_url)

data_from_net = response.json()

social_data = data_from_net['social_data']

total_salary_elder_35_peoples = 0.0
peoples_elder_35_years = 0
bad_debtors = 0
women_with_house = 0


class StrU(str):
    def tofloat(self):

        if (not self.replace('.', '1').isdigit()
                or self.count('.') > 1):

            return False

        else:

            return float(self)

    pass


for people in social_data:

    people_salary = StrU(people['salary'])
    people_payments = StrU(people['payments'])

    if people_salary.tofloat() is False or people_payments.tofloat() is False:

        print(f'Incorrect data from {people['name']}')

        sys.exit()

    people_salary = people_salary.tofloat()
    people_payments = people_payments.tofloat()

    if people['age'] > 35:

        peoples_elder_35_years += 1

        if people['are_many_kids'] is True:

            total_salary_elder_35_peoples += people_salary

    if people_payments > people_salary:

        bad_debtors += 1

    if people['gender'] == 'Жіноча' and people['is_own_housing'] is True:

        women_with_house += 1

result = f'Серед цих людей є:\
\n{women_with_house} жінки з власним житлом,\
\n{bad_debtors} людей у боргах,\
\n{peoples_elder_35_years} людей старших за 35 років.\
\nЗагальна зарплатня багатодітних людей старших за 35 років \
- {round(total_salary_elder_35_peoples)} гривень на місяць.'

print(result)

