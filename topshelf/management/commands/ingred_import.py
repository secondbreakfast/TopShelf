import requests

__author__ = 'zhila'
from django.http import request
from django.core.management.base import BaseCommand
from topshelf.models import IngredMaster

# This is the original import command I used to build my ingredient list. It pulled over 15k ingredients. Data was inconsistent and redundant, so I had to shelve this one for a different dataset.
# This data will be used to improve search results because it reflects exactly how data is entered into the Yummly recipe API.
# Once this data is normalized, it should be very powerful for searching through results.

#Special management command to do an initial data import from the Yummly API, to create a master list of ingredients.

class Command(BaseCommand):
    def handle(self, *args, **options):
        data = requests.get("http://api.yummly.com/v1/api/recipes?_app_id=935e1518&_app_key=b1f4ba0e9b7eb98208ed4a0d44d7cc83&facetField[]=ingredient")
        data = data.json()
        filtered = data["facetCounts"]["ingredient"]

        counter = 0
        for key, value in filtered.iteritems():
            if value > 5:
                IngredMaster.objects.create(ing = key)
                counter +=1
            # if counter == 10:
            #     break

