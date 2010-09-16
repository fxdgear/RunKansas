from django.http import HttpResponse
from runkansas.race.models import Race
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
    
def race_list(request):
    races = Race.objects.upcoming()
    
    return render_to_response("race/race_list.html", {
        'races': races,
    }, context_instance=RequestContext(request))
    
    


    