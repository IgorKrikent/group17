print('~' * 40)

# input data
user_name = input('Enter yon name >>> ').strip().title()
user_age = input('How old are you (years)? >>> ')

# data processing - age
if not user_age.isdigit():

    while not user_age.isdigit():
        user_age = input('''Please use integer data without other symbols
        (including spaces), so, how old are you? >>> ''')

user_age = int(user_age)

# input data - income
user_income = input('Your income per month (UAH) >>> ')

# data processing - income
if not user_income.replace(".","1").isdigit() or user_income.count(".") > 1:

    while not user_income.replace('.','1').isdigit() or user_income.count('.') > 1:

        user_income = input('''Please use integer or decimal without other symbols
so, what is your income? >>> ''')

user_income = float(user_income)

if user_age <= 65:

    time_is_a_money = 65 - user_age
    # money earned before retirement (dollars)
    dollars_earned = round((time_is_a_money * 12 * user_income) / 37.3)
    cars_earned = int(dollars_earned // 31_500)

    print(f'''
я, {user_name}, зможу заробити лише __{dollars_earned}__ долларів, 
що вистачить лише на __{cars_earned}__тойот, мене це не влаштовує,
тому я накуплю део-ланосів''')

else:
    print('\nна Тойоту вже не зароблю, зате в автобусі по пенсійному дешевше')

