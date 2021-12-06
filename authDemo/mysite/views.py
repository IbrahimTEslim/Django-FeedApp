from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import logout as django_logout

import json

# Create your views here.

def index(request):
    return render(request,'index.html')

def profile(request):
    user = request.user
    auth0_user=user.social_auth.get(provider='auth0')
    user_data={
        'user_id':auth0_user.uid,
        'name':user.first_name,
        'picture':auth0_user.extra_data['picture']
    }
    context = {
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user
    }
    return render(request,'profile.html',context)

def logout(request):
    django_logout(request)
    returnTo = 'http://127.0.0.1:8000'
    SOCIAL_AUTH_AUTH0_DOMAIN='dev-f2tvjhfm.us.auth0.com'
    SOCIAL_AUTH_AUTH0_KEY='HM6p0DokuBQMBcUWetrFY4gY3hajQHBD'

    return HttpResponseRedirect(f'http://{SOCIAL_AUTH_AUTH0_DOMAIN}/v2/logout?client_id={SOCIAL_AUTH_AUTH0_KEY}&returnTo={returnTo}')
