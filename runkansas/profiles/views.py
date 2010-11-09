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
from runkansas.profiles.forms import ProfileForm
from idios.views import group_and_bridge, group_context

@login_required
def profile_edit(request, **kwargs):
    """
    profile_edit
    """
    template_name = kwargs.pop("template_name", "idios/profile_edit.html")
    form_class = kwargs.pop("form_class", None)
    
    
    if request.is_ajax():
        template_name = kwargs.get(
            "template_name_facebox",
            "idios/profile_edit_facebox.html"
        )
    
    group, bridge = group_and_bridge(kwargs)
    
    # @@@ not group-aware (need to look at moving to profile model)
    profile = request.user.get_profile()
    
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect(profile.get_absolute_url(group=group))
    else:
        profile_form = ProfileForm(instance=profile)
    
    ctx = group_context(group, bridge)
    ctx.update({
        "profile": profile,
        "profile_form": profile_form,
    })
    
    return render_to_response(template_name, RequestContext(request, ctx))


@login_required
def my_ical(request, username):
    user = request.user.get_profile()
    response = MyRaceCalendar(user.races.all()).__call__()
    return response
