import requests
from dandhacontrol.models import AirportInfo
import time
import requests
from django.core.management.base import BaseCommand, CommandError

base_url='https://dandhacontrol.click'

a = AirportInfo.objects.filter(active=True)

def main():
    for m in a:



        params = {'airport__codeiataairport': str(m.codeiataairport)}

        response = requests.get( base_url + '/food', params=params)

        print(response.status_code)

        response = requests.get(base_url + '/spa', params=params)

        print(response.status_code)

        response = requests.get(base_url + '/lounge', params=params)

        print(response.status_code)

        response = requests.get(base_url + '/shopping', params=params)
        print(response.status_code)

        params = {'codeiataairport': str(m.codeiataairport)}
        response = requests.get(base_url + '/airport/exist', params=params)
        print(response.status_code)

        params = {'airport__codeiataairport': str(m.codeiataairport),
                  'for_him': True}
        response = requests.get(base_url + '/gift', params=params)

        print(response.status_code)

        params = {'airport__codeiataairport': str(m.codeiataairport),
                  'for_her': True}
        response = requests.get(base_url + '/gift', params=params)

        print(response.status_code)

        params = {'airport__codeiataairport': str(m.codeiataairport),
                  'for_kids': True}
        response = requests.get(base_url + '/gift', params=params)

        print(response.status_code)




class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        main()
