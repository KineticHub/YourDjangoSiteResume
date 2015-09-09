"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from .forms import NameForm

YOUR_INFO = {
    'name' : 'K. Alnajar',
    'bio' : 'If only physical books had a way to search them.',
    'email' : 'k.alnajar@cardisle.com',
    'twitter_username' : '@komptech',
    'github_username' : "kinetichub",
    'headshot_url' : 'https://pbs.twimg.com/profile_images/597865881977360385/WM01bNRd.png',
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['your_name']
            return render(request, 'app/draw.html', context_instance = RequestContext(request, {'name' : name,}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'app/name.html', {'form': form})
