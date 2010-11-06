from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from idios.models import ProfileBase

from runkansas.race.models import Race, Event

from django.contrib.auth.models import User
from timezones.fields import TimeZoneField

import datetime


class Profile(ProfileBase):
    
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    about = models.TextField(_("about"), null=True, blank=True)
    location = models.CharField(_("location"),
        max_length = 40,
        null = True,
        blank = True
    )
    website = models.URLField(_("website"),
        null = True,
        blank = True,
        verify_exists = False
    )
    
    races = models.ManyToManyField(Event, blank=True, null=True)

    class Meta:
        verbose_name = _("race profile")
        verbose_name_plural = _("race profiles")
    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self, group=None):
        return reverse("profile_detail", kwargs={
            "username": self.user.username
        })

    @property
    def upcoming_races(self):
	    return self.races.filter(date__gte=datetime.date.today())

    @property
    def completed_races(self):
	    return self.races.filter(date__lt=datetime.date.today())


def create_profile(sender, instance=None, **kwargs):
    if instance is None:
        return
    profile, created = Profile.objects.get_or_create(user=instance)


post_save.connect(create_profile, sender=User)
