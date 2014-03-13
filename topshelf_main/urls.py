from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
from tastypie.api import Api
from topshelf.api.resources import UserIngredResource

admin.autodiscover()

# v1_api = Api(api_name="v1")
# v1_api.register(UserIngredResource())

urlpatterns = patterns('',
    url(r'^$', 'topshelf.views.index', name='index'),
    
    url(r'^signup/', 'topshelf.views.signup', name="signup"),
    url(r'^accounts/login/', 'topshelf.views.login_page', name="login"),
    url(r'^accounts/logout/', 'topshelf.views.logout_page', name="logout"),
    url(r'^accounts/password/change/$', auth_views.password_change, name='password_change'),
    url(r'^accounts/password/change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^accounts/password/reset/$', auth_views.password_reset,
                name='password_reset'),
    url(r'^accounts/password/reset/done/$', auth_views.password_reset_done,
                name='password_reset_done'),
    url(r'^accounts/password/reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                auth_views.password_reset_confirm,
                name='password_reset_confirm'),

    url(r'accounts/', include('registration.backends.default.urls')),

#Add recipe detail page.
#     url(r'^pantry/', 'topshelf.views.pantry', name='pantry'),
    url(r'^(?P<user_id>\w+)/pantry/$', 'topshelf.views.pantry', name='pantry'),
    url(r'^(?P<user_id>\w+)/recipe/$', 'topshelf.views.recipe', name='recipe'),
    # url(r'^favorite/', 'topshelf.views.favorite', name='favorite'),

    # url(r'^api/', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'api/lecture/doc/',
    #     include('tastypie_swagger.urls', namespace='tastypie_swagger'),
    #     kwargs={"tastypie_api_module": "v1_api",
    #             "namespace": "lecture_tastypie_swagger"}
    # ),
)