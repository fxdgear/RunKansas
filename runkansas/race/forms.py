from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template.defaultfilters import slugify
from django.forms.formsets import BaseFormSet
from runkansas.race.models import Race, Distance, Event, RACE_CHOICES

class RaceForm(forms.Form):
    
    name = forms.CharField()
    date = forms.DateField()
    location = forms.CharField()
    url = forms.CharField(required=False)
    contact_name = forms.CharField()
    contact_phone = forms.CharField(required=False)
    contact_email = forms.CharField(required=False)
    race_type = forms.CharField(widget=forms.Select(choices=RACE_CHOICES))
    
    class Meta:
        model = Race
        exclude = ('slug', )
        
    def exists(self):
        name = self.cleaned_data['name']
        url = self.cleaned_data['url']
        race_type = self.cleaned_data['race_type']
        contact_email = self.cleaned_data['contact_email']
        contact_name = self.cleaned_data['contact_name']
        contact_phone = self.cleaned_data['contact_phone']
        location = self.cleaned_data['location']
        date = self.cleaned_data['date']
        
        try:
            return Race.objects.get(name=name, url=url, race_type=race_type,
                             contact_email=contact_email, contact_name=contact_name,
                             contact_phone=contact_phone, location=location, date=date)
        except:
            return False
        
            
    def save(self):
        race = Race()
        race.name = self.cleaned_data['name']
        race.slug = slugify(race.name)
        race.date = self.cleaned_data['date']
        race.location = self.cleaned_data['location']
        race.url = self.cleaned_data['url']
        race.contact_name = self.cleaned_data['contact_name']
        race.contact_phone = self.cleaned_data['contact_phone']
        race.contact_email = self.cleaned_data['contact_email']
        race.race_type = self.cleaned_data['race_type']        
        race.save()
        return race

class BaseEventFormSet(BaseFormSet):    
    def save(self, race):
        for form in self.forms:
            form.save(race)
            
class BaseDistanceFormSet(BaseFormSet):
    def save(self):
        for form in self.forms:
            form.save()
           
class EventForm(forms.Form):
    distance = forms.ModelChoiceField(queryset=Distance.objects.all(), label="Distance")
    date = forms.SplitDateTimeField()

    class Meta:
        model = Event
        exclude = ('race',)
        
    def save(self, race):
        event = Event()
        event.distance = self.cleaned_data['distance']
        event.date = self.cleaned_data['date']
        event.race = race
        event.save()

class DistanceForm(forms.ModelForm):
    title = forms.CharField(required=False)
    distance = forms.CharField(required=False)
    
    class Meta:
        model = Distance
        

