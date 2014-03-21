from django.contrib.auth.models import User
from django.db import models
# import datetime
# the names Ing and Ingred are used for ingredients. Typing ingredients constantly is just tiring.

# IngredMaster is a model with a ton of inconsistent data from the Yummly API.
# I want to normalize this data after the bootcamp, so I'm keeping it for now.
class IngredMaster(models.Model):
    ing = models.CharField(max_length=100)

    def __unicode__(self):
        return self.ing

# List of ingredients in the database, for users to select from.
class IngredMaster_test(models.Model):
    ing_test = models.CharField(max_length=100)

    def __unicode__(self):
        return self.ing_test

class UserIngred(models.Model):
    ing_master = models.ForeignKey(IngredMaster_test)
    # May need to add quantity, purchasedate, to intermediary table
    quantity = models.FloatField(null=True, blank=True)
    #Use default value for data entry?
    purch_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User)
    #Counts how many times that user has used the ingredient.
    count = models.IntegerField(default=1)

    def __unicode__(self):
        return self.ing_master.ing_test

class UserApiParams(models.Model):
    choice1 = models.CharField(max_length=50)
    choice2 = models.CharField(max_length=50, blank=True)
    choice3 = models.CharField(max_length=50, blank=True)
    diet = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User)

class SearchParams(models.Model):
    food_param = models.ForeignKey(UserIngred, related_name = 'food_param')
    diet = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.food_param.ing_master.ing_test


class UserRecipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    user = models.ForeignKey(User)

# #TO ADD LATER, AFTER BOOTCAMP: Add space for people to upload their own .
# class PersonalRecipes(models.Model):
#     recipe_name = models.CharField(max_length=100)
#     personalrecipe_ing = models.ForeignKey(ing_user)
