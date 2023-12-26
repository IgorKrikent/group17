visited_cities = input('Enter, separated by a space,'
                       ' the cities you have already visited'
                       ' over the past 10 years >>> ')

cities_to_visit = input('Enter, separated by a space,'
                        ' the cities which you want to visit'
                        ' in the next 10 years >>> ')


def input_to_set(user_data: str) -> set:
    """Converts user-typed lists into sets"""

    pretty_data = user_data.title().replace(',', '')

    result = set(pretty_data.split())

    return result


visited_cities_processed = input_to_set(visited_cities)
cities_to_visit_processed = input_to_set(cities_to_visit)

favorite_cities = visited_cities_processed & cities_to_visit_processed

if not favorite_cities:

    print("Looks like you're open to new travels")

else:

    proper_string_favorite_cities = ''

    for citi_name in favorite_cities:

        proper_string_favorite_cities += f'{citi_name}, '

    print(f"You probably really "
          f"liked {proper_string_favorite_cities.strip(', ')}")

