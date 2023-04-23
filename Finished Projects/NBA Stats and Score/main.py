from pprint import PrettyPrinter
from requests import get

baseUrl = "http://data.nba.net"
allJson = "/prod/v1/today.json"
printer = PrettyPrinter()


def getLinks():
    data = get(baseUrl + allJson).json()
    links = data["links"]
    return links


def getScoreboard():
    scoreboard = getLinks()["currentScoreboard"]
    data = get(baseUrl + scoreboard).json()["games"]
    for game in data:
        homeTeam = game["hTeam"]
        awayTeam = game["vTeam"]
        clock = game["clock"]
        period = game["period"]
        print("-" * 24)
        print(f"{homeTeam['triCode']} vs {awayTeam['triCode']}")
        print(f"{homeTeam['score']} - {awayTeam['score']}")
        print(f"{clock} - {period['current']}")


def getStats():
    stats = getLinks()["leagueTeamStatsLeaders"]
    # if season has started type "regularSeason" else type "preseason"
    teams = get(baseUrl + stats).json()["league"]["standard"]["preseason"]["teams"]
    teams = list(filter(lambda x: x["name"] != "Team", teams))
    teams.sort(key=lambda x: int(x["ppg"]["rank"]))
    for i, team in enumerate(teams):
        name = team["name"]
        nickname = team["nickname"]
        ppg = team["ppg"]["avg"]
        print(f"{i+1}. {name} - {nickname} - {ppg}")


while True:
    try:
        x = int(input("Enter Command [1. Get Scoreboard 2. Get Stats]: "))
        if x == 1:
            getScoreboard()
        elif x == 2:
            getStats()
        else:
            print("Invalid Command")
    except ValueError:
        print("Invalid Command")
