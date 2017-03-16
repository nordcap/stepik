def city_country(country, city):
    return city.title() + ', ' + country.title()


def city_country_population(country, city, population=''):
    if population:
        return city.title() + ', ' + country.title() + ', ' + str(population)
    else:
        return city.title() + ', ' + country.title()
