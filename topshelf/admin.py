from django.contrib import admin
from topshelf.models import IngredMaster, UserIngred
import autocomplete_light

class UserIngredAdmin(admin.ModelAdmin):
    # This will generate a ModelForm
    form = autocomplete_light.modelform_factory(UserIngred)

admin.site.register(UserIngred, UserIngredAdmin)
