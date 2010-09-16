from django.db import models
import datetime


class RaceManager(models.Manager):
    def upcoming(self):
        return self.filter(date__gte=datetime.datetime.today)

class Race(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    date = models.DateTimeField()
    location = models.TextField()
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    
    objects = RaceManager()
    
    def __unicode__(self):
        return self.name
    
class Distance(models.Model):
    UNIT_CHOICES = (
        (1, 'km'),
        (2, 'mi'),
        (3, 'meters'),
        (4, 'yards'),
    )
    
    title = models.CharField(max_length=40)
    distance = models.IntegerField()
    unit = models.IntegerField(choices=UNIT_CHOICES)
    
    def __unicode__(self):
        return self.title

class Event(models.Model):
    race = models.ForeignKey(Race)
    distance = models.ForeignKey(Distance)
    date = models.DateTimeField()
    
    def __unicode__(self):
        return "%s event for %s" % (self.distance, self.race)