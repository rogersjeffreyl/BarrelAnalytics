import urllib
import urllib2
import json
import re

access_token = 'fd746325fece9ef4576a98438baf41f9d68480e9'

def search(args):
    
    data = {}

    data['access_token'] = access_token
    data['query'] = args['query']
    data['cities'] = args['location']
    data['fields'] = 'title,description,aggregate_link,last_indexed_epoch'  #Change made here ROHAN
    data['limit'] = 10
    
    get_params = urllib.urlencode(data)

    endpoint = 'https://api-ssl.bitly.com/v3/search' + '?' + get_params
    response = urllib2.urlopen(endpoint)
    data = json.load(response)

    return data


def burst():
    
    data = {}

    data['access_token'] = access_token
    
    get_params = urllib.urlencode(data)

    endpoint = 'https://api-ssl.bitly.com/v3/realtime/bursting_phrases' + '?' + get_params
    response = urllib2.urlopen(endpoint)
    data = json.load(response)

    return data


def clicks(args):
    
    data = {}

    data['access_token'] = access_token
    data['link'] = args['url']
    data['rollup'] = 'false'
    data['unit'] = 'hour'
    data['units'] = 24    

    get_params = urllib.urlencode(data)

    endpoint = 'https://api-ssl.bitly.com/v3/link/clicks' + '?' + get_params
    response = urllib2.urlopen(endpoint)
    data = json.load(response)

    return data


def locations(args):
    
    data = {}

    data['access_token'] = access_token
    data['link'] = args['url']
    data['unit'] = 'hour'

    get_params = urllib.urlencode(data)

    endpoint = 'https://api-ssl.bitly.com/v3/link/countries' + '?' + get_params
    response = urllib2.urlopen(endpoint)
    data = json.load(response)

    return data
