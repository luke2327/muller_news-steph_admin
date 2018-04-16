from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from . import Database
from django.views.decorators.csrf import csrf_exempt
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
    query = 'SELECT CONCAT(player, "|" ,name) as player from swips_player_info'
    results = Database().get_data(query)
    result_p = []
    for row in results :
        result_p.append(row['player'])

    query = 'SELECT CONCAT(team, "|" ,name) as team from swips_team_info'
    results = Database().get_data(query)
    result_t = []
    for row in results :
        result_t.append(row['team'])

    query = 'SELECT CONCAT(league, "|" ,name) as league from swips_league_info'
    results = Database().get_data(query)
    result_l = []
    for row in results :
        result_l.append(row['league'])
    print(result_l)
    return HttpResponse(json.dumps({"players" : result_p, "leagues" : result_l, "teams" : result_t}))
@csrf_exempt
def news_relation(request) :
    print(request.method)
    if request.method == "POST":
        players = []
        teams = []
        leagues = []
        results = []
        for row in request.META.get('HTTP_PLAYERS').split(',') :
            try :
                players.append(int(row))
            except Exception as e:
                pass
        for row in request.META.get('HTTP_TEAMS').split(',') :
            try :
                teams.append(int(row))
            except Exception as e:
                pass
        for row in request.META.get('HTTP_LEAGUES').split(',') :
            try :
                leagues.append(int(row))
            except Exception as e:
                pass
        id = request.META.get('HTTP_ID')
        if len(leagues) + len(teams) + len(players) > 0 :
            values = []
            for row in players :
                values.append('("%s","%s","%s")' %(row, id, 'pl'))

            for row in teams :
                values.append('("%s","%s","%s")' %(row, id, 'te'))
            for row in leagues :
                values.append('("%s","%s","%s")' %(row, id, 'le'))
            query = 'INSERT INTO swips_news_relation (participant, news_id, type) VALUES %s' %(','.join(values))
            print(query)
            result = Database().insert_data(query)
            print(result)

            result_p = []
            result_t = []
            result_l = []
            try:
                query = 'SELECT CONCAT(name, "/" ,player) as player from swips_player_info WHERE player in (%s)' %(','.join(str(x) for x in players))
                results = Database().get_data(query)

                for row in results :
                    result_p.append(row['player'])
            except Exception as e :
                pass

            try:
                query = 'SELECT CONCAT(name, "/" ,team) as team from swips_team_info WHERE team in (%s)' %(','.join(str(x) for x in teams))
                results = Database().get_data(query)
                for row in results :
                    result_t.append(row['team'])
            except Exception as e:
                pass

            try:
                print(leagues)
                query = 'SELECT CONCAT(name, "/" ,league) as league from swips_league_info WHERE league in (%s)' %(','.join(str(x) for x in leagues))
                print(query)
                results = Database().get_data(query)
                for row in results :
                    result_l.append(row['league'])
            except Exception as e:
                pass

            return HttpResponse(json.dumps({"players" : result_p, "leagues" : result_l, "teams" : result_t}))

    elif request.method == "DELETE":
        id = request.META.get('HTTP_ID')
        following = request.META.get('HTTP_FOLLOWING')
        query = 'DELETE from swips_news_relation WHERE news_id = %s AND participant = %s ' %(id, following)
        print (query)
        results = Database().insert_data(query)
        return HttpResponse(status=200)
    return HttpResponse(status=200)

@csrf_exempt
def vods_relation(request) :
    print(request.method)
    if request.method == "POST":
        players = []
        teams = []
        leagues = []
        results = []
        for row in request.META.get('HTTP_PLAYERS').split(',') :
            try :
                players.append(int(row))
            except Exception as e:
                pass
        for row in request.META.get('HTTP_TEAMS').split(',') :
            try :
                teams.append(int(row))
            except Exception as e:
                pass
        for row in request.META.get('HTTP_LEAGUES').split(',') :
            try :
                leagues.append(int(row))
            except Exception as e:
                pass
        id = request.META.get('HTTP_ID')
        if len(leagues) + len(teams) + len(players) > 0 :
            values = []
            for row in players :
                values.append('("%s","%s","%s")' %(row, id, 'pl'))

            for row in teams :
                values.append('("%s","%s","%s")' %(row, id, 'te'))
            for row in leagues :
                values.append('("%s","%s","%s")' %(row, id, 'le'))
            query = 'INSERT INTO swips_vods_relation (participant, news_id, type) VALUES %s' %(','.join(values))
            print(query)
            result = Database().insert_data(query)
            print(result)

            result_p = []
            result_t = []
            result_l = []
            try:
                query = 'SELECT CONCAT(name, "/" ,player) as player from swips_player_info WHERE player in (%s)' %(','.join(str(x) for x in players))
                results = Database().get_data(query)

                for row in results :
                    result_p.append(row['player'])
            except Exception as e :
                pass

            try:
                query = 'SELECT CONCAT(name, "/" ,team) as team from swips_team_info WHERE team in (%s)' %(','.join(str(x) for x in teams))
                results = Database().get_data(query)
                for row in results :
                    result_t.append(row['team'])
            except Exception as e:
                pass

            try:
                print(leagues)
                query = 'SELECT CONCAT(name, "/" ,league) as league from swips_league_info WHERE league in (%s)' %(','.join(str(x) for x in leagues))
                print(query)
                results = Database().get_data(query)
                for row in results :
                    result_l.append(row['league'])
            except Exception as e:
                pass

            return HttpResponse(json.dumps({"players" : result_p, "leagues" : result_l, "teams" : result_t}))

    elif request.method == "DELETE":
        id = request.META.get('HTTP_ID')
        following = request.META.get('HTTP_FOLLOWING')
        query = 'DELETE from swips_vods_relation WHERE news_id = %s AND participant = %s ' %(id, following)
        print (query)
        results = Database().insert_data(query)
        return HttpResponse(status=200)
    return HttpResponse(status=200)
