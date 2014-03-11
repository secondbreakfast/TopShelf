from django.contrib import admin

# Register your models here.
from topshelf.models import IngredMaster, UserIngred

# # Need to allow admin search, because there are over 16k ingredients!!
# class Ingredients(admin.ModelAdmin):

admin.site.register(IngredMaster)
admin.site.register(UserIngred)
