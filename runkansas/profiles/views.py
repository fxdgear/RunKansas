from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from runkansas.profiles.feeds import MyRaceCalendar



@login_required
def my_ical(request, username):
    user = request.user.get_profile()
    response = MyRaceCalendar(user.races.all()).__call__()
    return response
