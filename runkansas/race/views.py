from django.http import HttpResponse, HttpResponseRedirect
from runkansas.race.models import Race, Event
from runkansas.race.forms import RaceForm, DistanceForm, EventFormSet
from django.forms.formsets import formset_factory
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import datetime

def current_month(request):
    race_list = Race.objects.upcoming_month()
    today = datetime.datetime.today()
    return render_to_response("race/race_archive_month.html",{
        'month': datetime.date(today.year,today.month, 1),
        'next_month': datetime.date(today.year, today.month+1, 1),
        'previous_month': datetime.date(today.year, today.month-1, 1),
        'object_list': race_list,
    }, context_instance=RequestContext(request))
    

def race_list(request):
    
    current_month = datetime.datetime.today().month
    races = Race.objects.upcoming()
    
    return render_to_response("race/race_list.html", {
        'races': races,
    }, context_instance=RequestContext(request))
    
    
def add_race(request):
    #DistanceFormset = formset_factory(DistanceForm, formset=BaseDistanceFormSet)

    if request.method == "POST":
        race_form = RaceForm(request.POST, prefix='race')
        #distance_formset = DistanceFormset(request.POST, prefix='distances')
        if race_form.is_valid():# and distance_formset.is_valid():
            if race_form.exists():
                return HttpResponse('Race Exists!') # Redirect after POST
            else:
                race = race_form.save()
                event_formset = EventFormSet(request.POST, instance=race, prefix='events')
                if event_formset.is_valid():
                    events = event_formset.save()
                url = race.get_absolute_url()
                return HttpResponseRedirect(url)
                return HttpResponse('Thanks for submitting a race!') # Redirect after POST
        else:
            #something went wrong
            pass
    else:
        race_form = RaceForm(prefix='race')
        
        event_formset = EventFormSet(prefix='events')
        #distance_formset = DistanceFormset(prefix='distances')
    
    
    return render_to_response('race/add_race.html',
           {
               'race_form': race_form,
               #'distance_formset': distance_formset,
               'event_formset': event_formset,
           },
           context_instance=RequestContext(request)
       )

    