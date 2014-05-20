from django.shortcuts import render_to_response
from django.template import RequestContext
from barrel.models import UserForm, BUser, Link,LinkData
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import bitly
import json
from random import  randint
def home(request):

    response_burst = bitly.burst()

    c = {
        'show_search_response': False,
        'response_burst': response_burst,
    }

    return render_to_response('index.html', c, context_instance=RequestContext(request))

def search(request):
    user_input = {}
    user_input['query'] = request.POST['query']
    user_input['location'] = request.POST['location']
    
    response_search = bitly.search(user_input)
    response_burst = bitly.burst()

    c = {
        'response_search': response_search,
        'response_burst': response_burst,
        'show_search_response': True,
        'response_found': len(response_search['data']['results']) > 0
        }

    return render_to_response('index.html', c, context_instance=RequestContext(request))

def save_link(request):
    buser1 = BUser.objects.get(buser_name = request.POST['user_name'])

    link = Link( url =  request.POST['new_link'], title = request.POST['title'])
    link.save()
    link.buser.add(buser1);

    all_buser_entries = BUser.objects.all()
    all_link_entries = Link.objects.all()
    print all_link_entries
    c = {'success': 1}

    return HttpResponse(json.dumps(c), mimetype='application/javascript')
    #return render_to_response('index.html', context_instance=RequestContext(request))

def rm_link(request):
    print request.POST['link']
    buser = BUser.objects.get(buser_name = request.POST['user_name'])

    #link = Link(buser = buser, url =  request.POST['link'], title = request.POST['link'])

    link=Link.objects.filter(buser__buser_name=request.POST['user_name'],url=request.POST['link'])
    link.delete()
    all_buser_entries = BUser.objects.all()
    all_link_entries = Link.objects.all()
    print all_link_entries
    c = {'success': 1}

    return HttpResponse(json.dumps(c), mimetype='application/javascript')

def dashboard(request):
    buser = BUser.objects.get(buser_name = request.GET['user_name'])
    all_links = Link.objects.filter(buser__buser_name = buser,)

    links_info = []

    for link in all_links:
        links_info.append({'title': link.title, 'url' : link.url})

    c = {
        'has_links': len(all_links) > 0,
        'links_info': links_info,
    }

    return render_to_response('dashboard.html', c, context_instance=RequestContext(request))

def show_clicks(request):
    args = {'url' : request.POST['link']}

    c = bitly.clicks(args)

    print c

    return HttpResponse(json.dumps(c), mimetype='application/javascript')

def show_clicks_true(request):
    args = {'url' : request.POST['link']}

    c=bitly.clicks_true(args)

    print c

    return HttpResponse(json.dumps(c), mimetype='application/javascript')

def show_locations(request):
    args = {'url' : request.POST['link']}
    print args
    c = bitly.locations(args)

    print c

    return HttpResponse(json.dumps(c), mimetype='application/javascript')
            
def show_referrers(request):
    args= {'url':request.POST['link']}
    print args
    c = bitly.referrers(args)

    print c

    return HttpResponse(json.dumps(c),mimetype='application/javascript')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            buser = BUser(buser_name = user.username)
            buser.save();

            registered = True
        else:
            print user_form.errors

    else:
        user_form = UserForm()

    c = {
        'user_form': user_form,
        'registered': registered,
        }


    return render_to_response('register.html', c, context_instance=RequestContext(request))


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Barrel account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context_instance=RequestContext(request))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def get_profile_trend(request):

    print "UNAMEl"

    links=Link.objects.filter(buser__buser_name=request.GET['user_name'])
    total_data=[]
    print links
    for link in links:
        link_data=LinkData.objects.all().filter(url=link.url).order_by('-time')
        click_values=[]
        social_score=[]

        for data in link_data:
            click_values.append([data.time.minute,data.click_rate])
            social_score.append([data.time.minute,data.click_rate])
        per_link_data={"name":link.url,"region":link.url,"population":click_values,"income":social_score,"lifeExpectancy":click_values}
        total_data.append(per_link_data)
    print total_data
    return HttpResponse(json.dumps(total_data), mimetype='application/javascript')


