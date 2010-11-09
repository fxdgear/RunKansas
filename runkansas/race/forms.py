from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template.defaultfilters import slugify
from runkansas.race.models import Race, Distance, Event, RaceType
from django.forms.models import inlineformset_factory, BaseInlineFormSet



class RaceForm(forms.ModelForm):
    
    date = forms.DateField()

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
        
            
    def save(self, commit=True):
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


EventFormSet = inlineformset_factory(Race, Event, extra=1)


class DistanceForm(forms.ModelForm):
    title = forms.CharField(required=False)
    distance = forms.CharField(required=False)
    
    class Meta:
        model = Distance
        

