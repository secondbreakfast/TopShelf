from django.contrib.auth.models import User
from django.db import models
# import datetime

#Add nutrition data to ingredient table, if I can find it. Allow search for diet?

# the names Ing and Ingred are used for ingredients. Typing ingredients constantly is just tiring.
class IngredMaster(models.Model):
    ing = models.CharField(max_length=100)

    def __unicode__(self):
        return self.ing

class IngredMaster_test(models.Model):
    ing_test = models.CharField(max_length=10000)

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

class UserRecipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    user = models.ForeignKey(User)

# #Add space for people to upload their own recipes
# class PersonalRecipes(models.Model):
#     recipe_name = models.CharField(max_length=100)
#     personalrecipe_ing = models.ForeignKey(ing_user)
