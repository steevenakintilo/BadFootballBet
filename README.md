
# BadFootballBet

All the info used for this project come from this websites: https://www.footmercato.net/ https://www.sportytrader.com/

## Requirements
To make the code work you will need to have Python and Pip installed in your computer

Link to download python: https://www.python.org/downloads/

Link to download pip: https://pip.pypa.io/en/stable/installation/

Link to download google chrome: https://www.google.com/intl/fr_fr/chrome/ 

For Auto Mode Only 

How to do a discord webhook? https://www.svix.com/resources/guides/how-to-make-webhook-discord/

Download all the modules required for the bot to work using this command:

```bash
    pip install -r requirements.txt
```

To start the bot just do

```bash
    python foot.py
```

## What this bot do ?

This bot have 2 modes: 
- "Stat of team" that will get the recent stats of a team depending on it's 20 last games.
- "Team vs Team" this mode will try to calculate the score of a Team A and a Team B based on it's last X recent games and will at the end tell the result between Team A and Team B Loose,Draw or Win.
  To get the best score possible the bot will give a default score of a team based on the power of it's league (for exemple a Premier League team will get the best score because it's the best league in the world) and it's position on the league then it will look into the last X games of the team and will also look into the last X games of each oppenents and will calculate a score based on several factor like: win, loose, home game, away game or if the team beaten was stronger...  then at the end it will get a final score and will reapeat the process for team B.
  Depending on the score of both team it will either display loose draw or win.

## How to use it ?

To use just do python foot.py then it will displayay a menu with three choices
![image](https://github.com/user-attachments/assets/962d1e41-7660-4699-aa84-d5f89cf3aa59)
If you choose 1 it will display the list of available country then you will need to choose ![image](https://github.com/user-attachments/assets/af4e3b1b-943d-4578-b578-51642d74b24d)
Then depending of your choice it will display all the team of the country ![image](https://github.com/user-attachments/assets/5cb4dac9-296c-4acf-a27b-7631770ab7a3)
And after it will do the same process for team B and then it will start to compare both teams and give you the result at the end.

If you choose 2 it will ask you the same things as choice 1 but for one team only then at the end will give you the stats of the team.

If you choose 3 it will just quit the program

# Auto Mode
Before using it make sure to put your webhook url into discordWebhookUrl.txt file
If you want to analyze all the games available of the next day just run 

```bash
    python autoFoot.py 1
```

```bash
    python autoFoot.py 2
```

```bash
    python autoFoot.py 3
```

```bash
    python autoFoot.py 4
```

```bash
    python autoFoot.py 5
```
Run each command on a different window/terminal prompt
It will analyze automaticaly all the game available of the day and will send all the result (Match,Winner,Percent and Odds) to your discord channel

Then If you want all the data on the .txt files just run printData.py and it will store all the data into result.txt,percent.txt,odds.txt and match.txt files 

## Result

Result of Arsenal VS Dortmund using only the last 3 games of each team (Test done the 21 December 2024)

![image](https://github.com/user-attachments/assets/bd4d3f6f-4a6e-434f-89aa-eed276633b05)

## Disclamer

This program was made for fun therefore the calculus are not 100% right and it will never be, it's impossible to guess the result of all the possible game.
Don't use this program to bet money you could loose money.
Afterall the calculus are made with real time stats to make the result as close as possible.

CR7 IS THE GOAT
