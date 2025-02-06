import pytest

from scrapData import *

S = Scraper()
team = "Liverpool"
allTeamTxt = print_file_info("allteam.txt").lower().split("\n")
team_pos = allTeamTxt.index(team.lower())

def test_one():
    assert 2 + 2 == 4

def test_match_of_the_day():
    assert len(get_match_of_the_day(S)) > 0

def test_has_Team_Played_since_september():
    assert has_Team_Played_since_september(S,team,allTeamTxt.index(team.lower()))

def test_get_odds():
    assert get_odds(S,"Bournemouth",team,"L",False,"01/02/2025")

def test_Position_Of_A_Team_On_Its_League():
    assert Position_Of_A_Team_On_Its_League(S,team) != -999

def test_Get_Last_X_Games_Result():
    assert Get_Last_X_Games_Result(S,team,team_pos,5)

def test_get_team_of_a_league():
    assert len(get_team_of_a_league(S,0)) > 3