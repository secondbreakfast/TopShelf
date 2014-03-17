__author__ = 'zhilabug'

import autocomplete_light
from topshelf.models import UserIngred

# This will generate a PersonAutocomplete class
autocomplete_light.register(UserIngred,
    # Just like in ModelAdmin.search_fields
    search_fields=['^ing_master'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    autocomplete_js_attributes={'placeholder': 'Type an ingredient',},
)