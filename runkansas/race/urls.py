from django.conf.urls.defaults import *
from django.views.generic.date_based import *
from django.conf import settings
from runkansas.race.models import Race

race_qs_dict = {
    'queryset': Race.objects.all(),
    'date_field': 'date',
    'allow_future': True,
}

urlpatterns = patterns('',
     (r'^$', archive_index, race_qs_dict, 'race_archive_index'),
     (r'^(?P<year>\d{4})/$', archive_year, race_qs_dict, 'race_archive_year'),
     (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', archive_month, race_qs_dict, 'race_archive_month'),
     (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', archive_day, race_qs_dict, 'race_archive_day'),
     (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', object_detail, race_qs_dict, 'race_detail'),
)
