from pygal_maps_world import i18n
from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    # returns the pygal 2 digit country code for the given country
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if the country wasnt found return none
    return None
