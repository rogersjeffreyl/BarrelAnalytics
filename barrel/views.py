from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import bitly

def home(request):
    c = {
        'show_response': False,
    }

    return render_to_response('index.html', c, context_instance=RequestContext(request))

def search(request):
    user_input = {}
    user_input['query'] = request.POST['query']
    user_input['location'] = request.POST['location']
    
    response = bitly.search(user_input)

    c = {
        'response': response,
        'show_response': True,
        'response_found': len(response['data']['results']) > 0
        }

    return render_to_response('index.html', c, context_instance=RequestContext(request))
