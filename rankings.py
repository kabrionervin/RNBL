from espn_api.basketball import League
import json

league = League(league_id = 924978122, year = 2025, espn_s2= 'AEBfyrWKGGBtwH8db6fxMt%2BzVJtYjpWe8NU3gKT7ITpM%2F75h%2Fjc12VfBPUSWiDx4n76FCTccIuQNR6rtAxShy3Oipl9zBd8Y74ITtLROTnfJINd6Pgdi4nrra8bB8bprfJ%2FpEXwBoFBqGKFkTi5UL%2FCvsMRpNNOoBPPZwKwIKLsYzZnYLjiRD2PGlazL39hi9NbUMZTM%2BKQt59CufHLJOmiLP2y3ajzjphpQUP%2F7HI9%2BR5%2FV4tJnCRA6diyjYUtwws4lLxX9NDRffTs%2F9MEMwqMuDdEwQI8ZoByIgnUqmV0yfA2A%2FtRKaJq83DEIdRvwonQ%3D', swid='{B0F9C9BF-8D39-4D39-84A0-8CBC6758E9CA}')

nba_schedule = {}

with open('nba_schedule.json') as json_file:
    nba_schedule = json.load(json_file)

gameDates = nba_schedule['leagueSchedule']['gameDates']

def getTeamGames(proTeam, week):
    gamesPlayed = 0
    for date in gameDates:
        if(date['games'][0]['weekNumber'] == week):
            for game in date['games']:
                if(game['homeTeam']['teamTricode'] == proTeam or game['awayTeam']['teamTricode'] == proTeam):
                    gamesPlayed += 1
    return gamesPlayed

print(getTeamGames('BOS', 2))
