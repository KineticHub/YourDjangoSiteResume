"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

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