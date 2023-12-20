import sub_library
import constants


def convert_cm_in_inches(cm_data: int | float) -> float:
    """accepts centimeters,
    converts in inches and rounds to 2 chars after coma;
    returns inches"""

    inch_data = cm_data * 2.54
    inch_result = round(inch_data, 2)

    return inch_result


def choose_pair_numbers_in_list(some_list: list) -> list:
    """Selects paired numbers from a list
    and returns them as a list"""

    list_of_double_numbers = []

    for element in some_list:

        if sub_library.is_double_number(element):

            list_of_double_numbers.append(element)

    return list_of_double_numbers


def is_solvent(*, total_repayment: int | float,
               salary: int | float) -> bool:
    """checks whether the monthly payment exceeds
    a certain percentage of income"""

    installment_period = sub_library.convert_input_in_float("Please \
enter installment period (in years)")

    number_of_payments = installment_period * constants.MONTHS_IN_YEAR
    pay_per_month = total_repayment/number_of_payments

    if pay_per_month < salary * constants.INCOME_RATIO:

        return True

    else:

        return False

