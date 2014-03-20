import urllib2
import requests
from bs4 import BeautifulSoup
import django.utils.encoding

__author__ = 'zhila'
from django.http import request
from django.core.management.base import BaseCommand
from topshelf.models import IngredMaster_test

#Special management command to do an initial data import from the Yummly API, to create a master list of ingredients.
# Users will be able to build their own ingredient lists using these values.

class Command(BaseCommand):
    def handle(self, *args, **options):
        # This site had a nice list of lots of ingredients, so I scraped it.
        data = urllib2.urlopen('http://www.food.com/library/all.zsp')
        food_data = BeautifulSoup(data, from_encoding='utf-8')
        data.close()

        ingredients = []
        for a in food_data.find_all('a'):
            ingredients.append(a.encode_contents())

        for item in ingredients:
            IngredMaster_test.objects.create(ing_test = item)