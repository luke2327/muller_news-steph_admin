from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from . import Database
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import requests
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
    import time
    start_time = time.time()
    results = Database().get_data(query)
    print('player  : %s' %(time.time()-start_time))
    result_p = []
    for row in results :
        result_p.append(row['player'])

    query = 'SELECT CONCAT(team, "|" ,name) as team from swips_team_info'
    start_time = time.time()
    results = Database().get_data(query)
    print('player  : %s' %(time.time()-start_time))
    result_t = []
    for row in results :
        result_t.append(row['team'])

    query = 'SELECT CONCAT(league, "|" ,name) as league from swips_league_info'
    start_time = time.time()
    results = Database().get_data(query)
    print('league  : %s' %(time.time()-start_time))
    result_l = []
    for row in results :
        result_l.append(row['league'])
    return HttpResponse(json.dumps({"players" : result_p, "leagues" : result_l, "teams" : result_t}))
@csrf_exempt
def best11(request) :
    if request.method == "POST":

        request_model = json.loads(str(request.body, "utf-8"))
        tournament = request_model['tournament']
        round = request_model['round']
        payload  = {'round_info': round, 'tournament': tournament, 'locale': 'en,ko,pt,vi,th,id'}
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

        response = requests.post("http://swips.co/preview/content_make/best11", data=payload)
        print(response)
        return HttpResponse(response)
    return HttpResponse(status=403)
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
    logging.error('vods_relation')
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
            query = 'INSERT INTO swips_vod_relation (participant, vod_id, type) VALUES %s' %(','.join(values))

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
        query = 'DELETE from swips_vod_relation WHERE vod_id = %s AND participant = %s ' %(id, following)

        results = Database().insert_data(query)
        return HttpResponse(status=200)
    return HttpResponse(status=200)
@csrf_exempt
def lineup(request) :
    if request.method == "POST":
        try :
            lineup = json.loads(str(request.body, "utf-8"))
            match_id = lineup['match_id']
            team1 = lineup['team1']
            team2 = lineup['team2']

            values = []

            for row in team1 :
                shirt_number = str(row['shirt_number'])
                if shirt_number is None or shirt_number == '' :
                    shirt_number = '0'
                position = str(row['position'])
                if position is None or position == '' :
                    position = ' '
                values.append('("%s", "%s", "%s", "%s", "%s", "%s")'
                        %(match_id, '1', row['lineup_number'], shirt_number,\
                          position, row['name']))

            for row in team2 :
                shirt_number = str(row['shirt_number'])
                if shirt_number is None or shirt_number == '' :
                    shirt_number = '0'
                position = str(row['position'])
                if position is None or position == '' :
                    position = ' '
                values.append('("%s", "%s", "%s", "%s", "%s", "%s")'
                        %(match_id, '2', row['lineup_number'], shirt_number,\
                          position, row['name']))

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
            request_model = json.loads(str(request.body, "utf-8"))

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
                query = ('UPDATE %s SET %s="%s", answer_ut = NOW(), status="answered" WHERE %s="%s" '
                    %(table, change_key, new_value, primary_key, primary_value))

            if db_type == 'admin' :
                result = Database().insert_data(query)
                if result > 0 :

                    return HttpResponse('200')
                else :
                    return HttpResponse(status=401)

    except Exception as e :
        return HttpResponse(status=401)
@csrf_exempt
def push_send(request) :
    try :
        if request.method == "POST":
            request_model = json.loads(str(request.body, "utf-8"))
            news_id = request_model['news_id']
            leagues = request_model['leagues']
            teams = request_model['teams']
            players = request_model['players']
            title = request_model['title']
            lang = request_model['lang']
            type = request_model['type']
            values = []
            langs = ['en', 'th', 'ko', 'vi', 'pt', 'id']
            if(type=='news'):
                for row in players :
                    values.append('CALL spocosy.swips_news_push_send("%s","%s","%s","%s"); '
                        %("pl", row, news_id, lang))
                for row in teams :
                    values.append('CALL spocosy.swips_news_push_send("%s","%s","%s","%s"); '
                        %("te", row, news_id, lang))
                for row in leagues :
                    values.append('CALL spocosy.swips_news_push_send("%s","%s","%s","%s"); '
                        %("le", row, news_id, lang))
            elif(type=='vod'):

                for row in players :
                    if lang is not None and lang != '' and lang!='None':
                        values.append('CALL spocosy.swips_vod_push_send("%s","%s","%s","%s"); '
                            %("pl", row, news_id, lang))
                    else :
                        for la in langs :
                            values.append('CALL spocosy.swips_vod_push_send("%s","%s","%s","%s"); '
                                %("pl", row, news_id, la))
                for row in teams :
                    if lang is not None and lang != '' and lang!='None':
                        values.append('CALL spocosy.swips_vod_push_send("%s","%s","%s","%s"); '
                            %("te", row, news_id, lang))
                    else :
                        for la in langs :
                            values.append('CALL spocosy.swips_vod_push_send("%s","%s","%s","%s"); '
                                %("te", row, news_id, la))
                for row in leagues :
                    if lang is not None and lang != '' and lang!='None':
                        values.append('CALL spocosy.swips_vod_push_send("%s","%s","%s","%s"); '
                            %("le", row, news_id, lang))
                    else :
                        for la in langs :
                            values.append('CALL spocosy.swips_vod_push_send("%s","%s","%s","%s"); '
                                %("le", row, news_id, la))
            result = 0
            for row in values :
                result += Database().insert_data(row)
            if result > 0 :
                return HttpResponse(json.dumps({"result" : 'ok'}))
            else :
                return HttpResponse(status=401)
    except Exception as e :
        logging.error(e)
        return HttpResponse(status=401)

@csrf_exempt
def push_send_transfer(request) :
    try :
        if request.method == "POST":
            request_model = json.loads(str(request.body, "utf-8"))
            team = request_model['team']
            following = request_model['following']
            transfer_id = request_model['transfer_id']
            player_name = request_model['player_name']
            from_team_name = request_model['from_team_name']
            to_team_name = request_model['to_team_name']
            transfer_type = request_model['transfer_type']
            is_loan = request_model['is_loan']
            team_names = from_team_name + ';' + to_team_name
            if int(team) <= 1:
                participant_type = "te"
            else :
                return HttpResponse(status=401)

            if transfer_type == 'official' and int(is_loan) != 1:
                push_type = 11
            elif transfer_type == 'rumor' and int(is_loan) != 1:
                push_type = 111
            elif transfer_type == 'official' and int(is_loan) == 1:
                push_type = 211
            elif transfer_type == 'rumor' and int(is_loan) == 1:
                push_type = -1
            query = ('INSERT INTO swips_push '
                '(push_type, table_name, row_id, status, '
                'ref1, ref2, ref3, ref4, ref5, refstr1, refstr2, refstr3) '
                'VALUE ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'
                %(push_type, 'swips_transfer_push_send', transfer_id, 'ready', following,
                transfer_id, team, 0, 0, participant_type, team_names, player_name))
            result = Database().insert_data(query)
            if result > 0 :
                return HttpResponse(json.dumps({"result" : 'ok'}))
            else :
                return HttpResponse(status=401)
    except Exception as e :
        logging.error(e)
        return HttpResponse(status=401)
