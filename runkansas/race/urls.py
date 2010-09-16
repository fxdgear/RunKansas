from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('runkansas.race.views',
    (r'^$', 'current_datetime'),
    (r'foo/', 'race_list')
)
