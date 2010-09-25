from django.http import HttpResponse
from runkansas.race.models import Race
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
    
    


    