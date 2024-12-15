class teamData:
    frenchTeam = """
    PSG
    Marseille
    Monaco
    Lille
    Lyon
    Nice
    Lens
    Auxerre
    Reims
    Toulouse
    Brest
    Rennes
    Nantes
    Strasbourg
    Angers
    ASSE
    Le Havre
    Montpellier
    """.lower().split("\n")

    englishTeam = """
    Liverpool
    Chelsea
    Arsenal
    Man City
    Nottingham
    Aston Villa
    Brighton
    Bournemouth
    Brentford
    Fulham
    Tottenham
    Newcastle
    Man United
    West Ham
    Everton
    Leicester
    Crystal Palace
    Ipswich
    Wolverhampton
    Southampton
    """.lower().split("\n")

    spanishTeam = """
    Barcelone
    Real Madrid
    Atlético
    Bilbao
    Villarreal
    Real Sociedad
    Osasuna
    Majorque
    Girona
    Celta Vigo
    Betis
    Vallecano
    Séville
    Las Palmas
    Getafe
    Alavés
    Leganes
    Espanyol
    Valence
    Valladolid
    """.lower().split("\n")

    italianTeam = """
    Atalanta
    Naples
    Inter Milan
    Fiorentina
    Lazio
    Juventus
    Milan
    Bologne
    Udinese
    Empoli
    Rome
    Torino
    Parme
    Genoa
    Cagliari
    Lecce
    Côme
    Hellas
    Monza
    Venise
    """.lower().split("\n")

    germanTeam = """
    Bayern Munich
    Francfort
    Leverkusen
    Leipzig
    Wolfsbourg
    Dortmund
    Fribourg
    Stuttgart
    Mayence
    Brême
    M'gladbach
    Union Berlin
    Augsbourg
    Hoffenheim
    Sankt Pauli
    Heidenheim
    Kiel
    Bochum
    """.lower().split("\n")

    portugalTeam = """
    Sporting
    Benfica
    Porto
    Santa Clara
    Braga
    Vitória SC
    Moreirense
    Famalicão
    Rio Ave
    Casa Pia
    Estoril
    Gil Vicente
    Estrela
    Boavista
    AVS
    Nacional
    Farense
    Arouca
    """.lower().split("\n")

    netherlandTeam = """
    PSV
    Utrecht
    Ajax
    Feyenoord
    Twente
    AZ
    NAC
    Go Ahead
    Fortuna
    Heerenveen
    NEC
    Willem II
    Zwolle
    Groningen
    Heracles
    Sparta
    Waalwijk
    Almere
    """.lower().split("\n")

    belgiumTeam = """
    Genk
    Club Bruges
    Anderlecht
    Antwerp
    La Gantoise
    Malines
    R. Union SG
    Standard
    Westerlo
    Charleroi
    Dender
    Louvain
    Saint-Trond
    Courtrai
    Cercle Bruges
    Beerschot
    """.lower().split("\n")

    turkishTeam = """
    Galatasaray
    Fenerbahce
    Samsunspor
    Eyüp
    Besiktas
    Goztepe
    Basaksehir
    Konyaspor
    Rize
    Gaziantep FK
    Sivasspor
    Antalyaspor
    Trabzon
    Kasımpaşa
    Kayseri
    Alanya
    Bodrum
    Hatay
    Demirspor
    """.lower().split("\n")

    swissTeam = """
    Lugano
    Bâle
    Servette
    Lausanne
    Zurich
    Lucerne
    Sion
    Saint-Gall
    Young Boys
    Yverdon
    Winterthour
    GC Zurich
    """.lower().split("\n")

    allTeam_ = [englishTeam,spanishTeam,italianTeam,germanTeam,frenchTeam,portugalTeam,netherlandTeam,turkishTeam,belgiumTeam,swissTeam]

    allTeam = []
    
    NB_OF_TEAM_ENGLISH = len(englishTeam) - 2
    NB_OF_TEAM_SPANISH = len(spanishTeam) - 2
    NB_OF_TEAM_ITALIAN = len(italianTeam) - 2
    NB_OF_TEAM_GERMAN = len(germanTeam) - 2
    NB_OF_TEAM_FRENCH = len(frenchTeam) - 2
    NB_OF_TEAM_PORTUGAL = len(portugalTeam) - 2
    NB_OF_TEAM_NETHERLAND = len(netherlandTeam) - 2
    NB_OF_TEAM_TURKISH = len(turkishTeam) - 2
    NB_OF_TEAM_BELGIUM = len(belgiumTeam) - 2
    NB_OF_TEAM_SWISS = len(swissTeam) - 2
    
    ENGLISH = 300 * 5
    SPANISH = 295 * 4.8
    ITALIAN = 290 * 4.6
    GERMAN = 285 * 4.4
    FRENCH = 280 * 4.2
    PORTUGAL = 270 * 4
    NETHERLAND = 265 * 3.5
    TURKISH = 260 * 3
    BELGIUM = 250 * 2
    SWISS = 220 * 1.2
    NONE = 10
    
    default_score_based_on_the_league = [ENGLISH,SPANISH,ITALIAN,GERMAN,FRENCH,PORTUGAL,NETHERLAND,TURKISH,BELGIUM,SWISS,NONE]
    nb_of_team_on_all_league = [NB_OF_TEAM_ENGLISH,NB_OF_TEAM_SPANISH,NB_OF_TEAM_ITALIAN,NB_OF_TEAM_GERMAN,NB_OF_TEAM_FRENCH,NB_OF_TEAM_PORTUGAL,NB_OF_TEAM_NETHERLAND,NB_OF_TEAM_TURKISH,NB_OF_TEAM_BELGIUM,NB_OF_TEAM_SWISS]
    pos_league_team = 0
    #print("dodod " , nb_of_team_on_all_league)
    for team in allTeam_:
        for lilTeam in team:
            if len(lilTeam.strip().replace(" ","-")) > 1:
                allTeam.append(lilTeam.strip().replace(" ","-"))

    all_league_url = ["https://www.footmercato.net/club/liverpool/classement",
                      "https://www.footmercato.net/club/fc-barcelone/classement",
                      "https://www.footmercato.net/club/inter/classement",
                      "https://www.footmercato.net/club/bayer-04-leverkusen/classement",
                      "https://www.footmercato.net/club/psg/classement",
                      "https://www.footmercato.net/club/sporting-clube-de-portugal/classement",
                      "https://www.footmercato.net/club/feyenoord-rotterdam/classement",
                      "https://www.footmercato.net/club/galatasaray-spor-kulubu/classement",
                      "https://www.footmercato.net/club/club-brugge-kv/classement",
                      "https://www.footmercato.net/club/bsc-young-boys/classement"]
    
    all_league_name = ["Premiere League","Liga","Serie A","Bundesliga","League 1","Liga Portugal","Eredivise","Super Lig Türkiye","Jupiter Pro League","Super Lig Switzerland"]
    country_of_the_team = ["England","Spain","Italy","France","Germany","Portugal","Netherland","Turkiye","Belgium","Switzerland"]


class TeamStat:
    name = ""
    point = 0
    pos_on_the_league = ""
    league_of_the_team = ""
    last_x_game_list = []
    last_x_game_win = []
    last_x_game_draw = []
    last_x_game_loose = []
    last_x_game_list_score = []
    last_x_game_win_score = []
    last_x_game_draw_score = []
    last_x_game_loose_score = []
    
    nb_of_win = 0
    nb_of_loose = 0
    nb_of_draw = 0
    nb_of_game = 0
    win_rate_percent = 0
    loose_rate_percent = 0
    draw_rate_percent = 0
    nb_of_goal_scored = 0
    nb_of_goal_conceded = 0
    nb_of_goal_scored_per_match = 0
    nb_of_goal_conceded_per_match = 0
    last_x_game_list_league_or_not = []
    last_x_game_win_league_or_not = []
    last_x_game_draw_league_or_not = []
    last_x_game_loose_league_or_not = []
    
    last_x_game_list_away_or_home = []
    
    nb_of_win_away = 0
    nb_of_loose_away = 0
    nb_of_draw_away = 0
    nb_of_game_away = 0
    win_rate_percent_away = 0
    loose_rate_percent_away = 0
    draw_rate_percent_away = 0
    last_x_game_away_list = []
    last_x_game_away_score = []
    
    nb_of_goal_scored_away = 0
    nb_of_goal_conceded_away = 0
    nb_of_goal_scored_per_match_away = 0
    nb_of_goal_conceded_per_match_away = 0
    
    nb_of_win_home = 0
    nb_of_loose_home = 0
    nb_of_draw_home = 0
    nb_of_game_home = 0
    win_rate_percent_home = 0
    loose_rate_percent_home = 0
    draw_rate_percent_home = 0
    last_x_game_home_list = []
    last_x_game_home_score = []
    
    
    nb_of_goal_scored_home = 0
    nb_of_goal_conceded_home = 0
    nb_of_goal_scored_per_match_home = 0
    nb_of_goal_conceded_per_match_home = 0
    
    last_x_game_win_draw_or_loose = []
    last_x_game_win_draw_or_loose_away = []
    last_x_game_win_draw_or_loose_home = []
    
    