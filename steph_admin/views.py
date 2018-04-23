from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from . import Database
from django.views.decorators.csrf import csrf_exempt
import json
import logging
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
    return HttpResponse(json.dumps({"players" : result_p, "leagues" : result_l, "teams" : result_t}))
@csrf_exempt
def news_relation(request) :

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

            result = Database().insert_data(query)


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
                query = 'SELECT CONCAT(name, "/" ,league) as league from swips_league_info WHERE league in (%s)' %(','.join(str(x) for x in leagues))


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

        results = Database().insert_data(query)
        return HttpResponse(status=200)
    return HttpResponse(status=200)

@csrf_exempt
def vods_relation(request) :
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

            result = Database().insert_data(query)


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
                query = 'SELECT CONCAT(name, "/" ,league) as league from swips_league_info WHERE league in (%s)' %(','.join(str(x) for x in leagues))

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

        results = Database().insert_data(query)
        return HttpResponse(status=200)
    return HttpResponse(status=200)
@csrf_exempt
def lineup(request) :
    if request.method == "POST":
        try :
            lineup = json.loads(request.body)
            match_id = lineup['match_id']
            team1 = lineup['team1']
            team2 = lineup['team2']

            values = []

            for row in team1 :
                values.append('("%s", "%s", "%s", "%s", "%s", "%s")'
                        %(match_id, '1', row['lineup_number'], row['shirt_number'],\
                          row['position'], row['name']))

            for row in team2 :
                values.append('("%s", "%s", "%s", "%s", "%s", "%s")'
                        %(match_id, '2', row['lineup_number'], row['shirt_number'],\
                          row['position'], row['name']))

            query = ('INSERT INTO swips_lineup_custom '
                '(match_id, team, lineup_number, shirt_number, position, name) '
                'VALUES %s' %(','.join(values)))

            result = Database().insert_data(query)
            if result > 0 :
                return HttpResponse(json.dumps({"result" : 201}))
            else :
                return HttpResponse(status=403)
        except Exception as e :
            return HttpResponse(status=401)
    return HttpResponse(status=500)
@csrf_exempt
def one_value_change(request) :
    try :
        if request.method == "POST":
            request_model = json.loads(request.body)

            db_type = request_model['db_type']
            table = request_model['table']
            primary_key = request_model['primary_key']
            primary_value = request_model['primary_value']
            change_key = request_model['change_key']
            default_value = request_model['default_value']
            new_value = request_model['new_value']

            query = ('UPDATE %s SET %s="%s" WHERE %s="%s" '
                %(table, change_key, new_value, primary_key, primary_value))

            if table == 'swips_qna' and change_key == 'answer' and new_value != '' :
                query = ('UPDATE %s SET %s="%s", answer_ut = NOW(), status="ready" WHERE %s="%s" '
                    %(table, change_key, new_value, primary_key, primary_value))

            if db_type == 'admin' :
                result = Database().insert_data(query)
                if result > 0 :
                    return HttpResponse(json.dumps({"result" : 'ok'}))
                else :
                    return HttpResponse(status=401)

    except Exception as e :
        return HttpResponse(status=401)
@csrf_exempt
def push_send(request) :
    try :
        if request.method == "POST":
            logging.error('step1')
            request_model = json.loads(str(request.body, "utf-8"))
            logging.error('step1-1')
            news_id = request_model['news_id']
            leagues = request_model['leagues']
            teams = request_model['teams']
            players = request_model['players']
            title = request_model['title']
            lang = request_model['lang']
            type = request_model['type']
            values = []
            if(type=='news'):
                push_type = 1
                table_name = 'curry_news_push_send'
            elif(type=='vod'):
                push_type = 102
                table_name = 'curry_vod_push_send'
            for row in players :
                values.append('("%s", "%s", '
                    '"%s", "ready", "%s", "%s", '
                    '"1", "0", "0", "%s", "pl", "%s")'
                    %(push_type, table_name, news_id, row, news_id, lang, title))
            for row in teams :
                values.append('("%s", "%s", '
                    '"%s", "ready", "%s", "%s", '
                    '"1", "0", "0", "%s", "pl", "%s")'
                    %(push_type, table_name, news_id, row, news_id, lang, title))
            for row in leagues :
                values.append('("%s", "%s", '
                    '"%s", "ready", "%s", "%s", '
                    '"1", "0", "0", "%s", "pl", "%s")'
                    %(push_type, table_name, news_id, row, news_id, lang, title))

            query = ('INSERT INTO swips_push '
                '(push_type, table_name, row_id, status, ref1, ref2, ref3, ref4, ref5, refstr1, refstr2, refstr3) '
                'VALUES %s' %(','.join(values)))
            result = Database().insert_data(query)
            if result > 0 :
                logging.error('step2')
                return HttpResponse(json.dumps({"result" : 'ok'}))
            else :
                return HttpResponse(status=401)
    except Exception as e :
        logging.error(e)
        return HttpResponse(status=401)
