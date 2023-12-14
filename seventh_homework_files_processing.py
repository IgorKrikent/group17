with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:

    file.seek(0)

    # for row in file.readlines():
    #
    #     row_list = row.split(';')
    #
    #     if row_list[5] == 'UA':
    #
    #         print(row_list[2])

    # Annother aproach

    # Check variable
    i = 0

    while True:

        line = file.readline().split(';')

        i += 1

        if not line or line == ['']:

            print(f'{i-1} lines processed')

            break

        elif line[5] == 'UA':

            print(line[2])

