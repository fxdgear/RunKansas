from django.db import models
import datetime


class RaceManager(models.Manager):
    def upcoming(self):
        return self.filter(date__gte=datetime.datetime.today())
        
    def upcoming_month(self):
        today = datetime.datetime.today()
        return self.filter(date__year=today.year, date__month=today.month, date__gte=today)
        
    def current_month(self):
        today = datetime.datetime.today()
        return self.filter(date__year=today.year, date__month=today.month)


RACE_CHOICES=(
    (1, "Trail"),
    (2, "Road"),
    (3, "Mix"),
    )

class Race(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField()
    date = models.DateTimeField()
    location = models.TextField()
    url = models.URLField(blank=True, null=True)
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    race_type = models.IntegerField(choices=RACE_CHOICES, blank=True, null=True)
    
    objects = RaceManager()
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('race_detail', (), {
            'year': self.date.year,
            'month': self.date.strftime('%b').lower(),
            'day': self.date.strftime('%d'),
            'slug': self.slug
        })
    
    @property
    def events(self):
        return self.event_set.all()
        
    @property
    def type(self):
        for i,t in RACE_CHOICES:
            if self.race_type == i:
                return t
        
        
    
class Distance(models.Model):
    UNIT_CHOICES = (
        (1, 'km'),
        (2, 'mi'),
        (3, 'meters'),
        (4, 'yards'),
    )
    
    title = models.CharField(max_length=40)
    distance = models.DecimalField(max_digits=10, decimal_places=1)
    unit = models.IntegerField(choices=UNIT_CHOICES)
    
    def __unicode__(self):
        return self.title

class Event(models.Model):
    race = models.ForeignKey(Race)
    distance = models.ForeignKey(Distance)
    date = models.DateTimeField()
    
    def __unicode__(self):
        return "%s event for %s" % (self.distance, self.race)