from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from . import Database
import json
# Create your views here.
def players(request):
    query = 'SELECT CONCAT(id, "|" ,name) as player from swips_player'
    results = Database().get_data(query)
    result = []
    for row in results :
        result.append(row['player'])
    return HttpResponse(json.dumps({"result" : result}))

def followings(request):
    query = 'SELECT CONCAT(id, "|" ,name) as player from swips_player'
    results = Database().get_data(query)
    result_p = []
    for row in results :
        result_p.append(row['player'])

    query = 'SELECT CONCAT(id, "|" ,name) as team from swips_team'
    results = Database().get_data(query)
    result_t = []
    for row in results :
        result_t.append(row['team'])

    query = 'SELECT CONCAT(id, "|" ,name) as league from swips_league'
    results = Database().get_data(query)
    result_l = []
    for row in results :
        result_l.append(row['league'])
    print(result_l)
    return HttpResponse(json.dumps({"players" : result_p, "leagues" : result_l, "teams" : result_t}))
