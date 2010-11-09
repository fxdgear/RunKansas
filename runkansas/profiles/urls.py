from django.conf.urls.defaults import *
from idios.urls import urlpatterns as idios_urls


runks_patterns = patterns("",
    url(r"^edit/$", "runkansas.profiles.views.profile_edit", name="profile_edit"),
    url(r"^profile/(?P<username>[\w\._-]+)/ical/$", "runkansas.profiles.views.my_ical", name="my_ical"),
)

urlpatterns = runks_patterns + idios_urls
