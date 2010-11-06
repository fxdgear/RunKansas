from django.conf.urls.defaults import *



urlpatterns = patterns("",
    url(r"^username_autocomplete/$", "runkansas.autocomplete_app.views.username_autocomplete_friends", name="profile_username_autocomplete"),
    url(r"^$", "runkansas.profiles.views.profiles", name="profile_list"),
    url(r"^profile/(?P<username>[\w\._-]+)/$", "runkansas.profiles.views.profile", name="profile_detail"),
    url(r"^edit/$", "runkansas.profiles.views.profile_edit", name="profile_edit"),
)
