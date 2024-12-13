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

    allTeam_ = [frenchTeam,englishTeam,spanishTeam,germanTeam,italianTeam,portugalTeam,netherlandTeam,turkishTeam,belgiumTeam,swissTeam]

    allTeam = []
    
    
    NB_OF_TEAM_ENGLISH = len(englishTeam)
    NB_OF_TEAM_SPANISH = len(spanishTeam)
    NB_OF_TEAM_ITALIAN = len(italianTeam)
    NB_OF_TEAM_GERMAN = len(germanTeam)
    NB_OF_TEAM_FRENCH = len(frenchTeam)
    NB_OF_TEAM_PORTUGAL = len(portugalTeam)
    NB_OF_TEAM_NETHERLAND = len(netherlandTeam)
    NB_OF_TEAM_TURKISH = len(turkishTeam)
    NB_OF_TEAM_BELGIUM = len(belgiumTeam)
    NB_OF_TEAM_SWISS = len(swissTeam)
    
    ENGLISH = 10
    SPANISH = 9
    ITALIAN = 8
    GERMAN = 7
    FRENCH = 6
    PORTUGAL = 5
    NETHERLAND = 4
    TURKISH = 3
    BELGIUM = 2
    SWISS = 1
    NONE = 0
    
    for team in allTeam_:
        for lilTeam in team:
            if len(lilTeam.strip().replace(" ","-")) > 1:
                allTeam.append(lilTeam.strip().replace(" ","-"))
