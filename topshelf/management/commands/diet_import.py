__author__ = 'zhila'

import requests

__author__ = 'zhila'
from django.http import request
from django.core.management.base import BaseCommand
# from topshelf.models import DietMaster

# Special management command to do an initial data import from the Yummly API, to create a master list of ingredients.
# Users will be able to build their own ingredient lists using these values. This isn;t being used now but will be later so that users can filter recipes by diet and allergies.

# The master record for Diet doesn't exist yet, but it will later. This will be a really cool feature.
class Command(BaseCommand):
    def handle(self, *args, **options):
        data = requests.get("http://api.yummly.com/v1/api/recipes?_app_id=935e1518&_app_key=b1f4ba0e9b7eb98208ed4a0d44d7cc83&facetField[]=diet")
        data = data.json()
        filtered = data["facetCounts"]["diet"]
        counter = 0
        for key, value in filtered.iteritems():
            if value > 2:
                DietMaster.objects.create(diet = key)
                counter +=1

