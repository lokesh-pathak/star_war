import swapi
import json
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
        : Create managment (python manage.py create_users) command for enter the user data into  datbase.
        : Insert static email and password into auth user table.
    """
    args = '';

    def write_to_json_file(self, fileName, data):
        with open(fileName + '.json', 'w') as fp:
            json.dump(data, fp)
            print("Loading {} data completed....".format(fileName))

    def get_planets(self):
        print("Loading Planets data....")
        data = {};
        data['planets'] = []
        planets = swapi.get_all("planets")
        for planet in planets.order_by("name"):
            data['planets'].append(planet.name)
        self.write_to_json_file('planets', data)

    def get_films(self):
        print("Loading Movies data....")
        data = {};
        data['films'] = []
        films = swapi.get_all("films")
        for film in films.order_by("title"):
            data['films'].append(film.title)
        self.write_to_json_file('films', data)

    def handle(self, *args, **options):
        print("loading data. Please wait for while .....")
        self.get_planets()
        self.get_films()
