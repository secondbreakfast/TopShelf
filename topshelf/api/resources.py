from django.conf import settings
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, CharField, ToOneField
from tastypie.resources import ModelResource, Resource
from topshelf.models import IngredMaster, UserIngred, UserRecipe

# Limit post, delete, etc to only the admin?
class BareIngredientResource(ModelResource):
    class Meta:
        queryset = IngredMaster.objects.all()
        resource_name = "master_ingredient"
        authorization = Authorization()

class UserIngredResource(ModelResource):
    ingred = ToManyField(BareIngredientResource, "ing_master", null=True)

    class Meta:
        queryset = UserIngred.objects.all()
        resource_name = "user_ingredient"
        authorization = Authorization()

class UserRecipeResource(ModelResource):
    ingred = ToManyField(BareIngredientResource, "ingred", null=True)

    class Meta:
        queryset = UserRecipe.objects.all()
        resource_name = "user_favorites"
        authorization = Authorization()

######################
# Non-Model Resource #
######################

class Version(object):
    def __init__(self, identifier=None):
        self.identifier = identifier


class VersionResource(Resource):
    identifier = CharField(attribute='identifier')

    class Meta:
        resource_name = 'version'
        allowed_methods = ['get']
        object_class = Version
        include_resource_uri = False

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.identifier
        else:
            kwargs['pk'] = bundle_or_obj['identifier']

        return kwargs

    def get_object_list(self, bundle, **kwargs):
        return [Version(identifier=settings.VERSION)]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle, **kwargs)