import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup

def get_primary_name(alternate_names,name):
    for names_list in alternate_names:
        for val in names_list:
            if val == name:
                return names_list[0]
    for names_list in alternate_names:
        if names_list[0].find(name)!=-1:
            return names_list[0]
        


def get_playerstats(url):
    page = requests.get(url).text
    bs = BeautifulSoup(page,'html.parser')

    player_stats={}
    alternate_names=[]

    # Getting table from page
    table_body=bs.find_all('tbody')
    
    # Get First Innings Batting details
    rows = table_body[0].find_all('tr')
    for row in rows[::2]:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        if cols[0] == 'Extras':
            continue
        else:
            stats = {"Runs Scored":0, "Balls Faced":0, "Fours":0, "Sixes":0, "Strike Rate":0, "Dismissal":"Did Not Bat", "Overs Bowled":0, "Maidens":0, "Runs Conceded":0, "Wickets":0, "LBW/Bowled Wickets":0, "Economy":0, "Wides":0, "No Balls":0, "Catches":0, "Direct Throw Runout":0, "Runout involving Thrower and Catcher":0 }
            name = re.sub(r"\W+", ' ', cols[0].split("(c)")[0]).strip()
            names = []
            names.append(name)
            splitted_name = name.split()
            if len(splitted_name)>1:
                new_name = splitted_name[0][0]+" "+splitted_name[-1]
                names.append(new_name)
                new_name = splitted_name[-1]
                names.append(new_name)
            alternate_names.append(names)
            stats["Runs Scored"] = int(cols[2])
            stats["Balls Faced"] = int(cols[3])
            stats["Fours"] = int(cols[5])
            stats["Sixes"] = int(cols[6])
            stats["Strike Rate"] = float(cols[7])
            stats["Dismissal"] = cols[1].replace("†","")
            player_stats[name] = stats

    # Getting players which didn't bat
    dnb_row = bs.find_all("tfoot")[0].find_all("div")
    for c in [dnb_row[0]]:
        if str(c).find("Fall of wickets")!=-1:
            break
        dnb_cols = c.find_all('span')
        dnb = [x.text.strip().split("(c)")[0] for x in dnb_cols]
        dnb = filter(lambda item: item, [re.sub(r"\W+", ' ', x).strip() for x in dnb])
        for dnb_batsman_name in dnb:
            stats = {"Runs Scored":0, "Balls Faced":0, "Fours":0, "Sixes":0, "Strike Rate":0, "Dismissal":"Did Not Bat", "Overs Bowled":0, "Maidens":0, "Runs Conceded":0, "Wickets":0, "LBW/Bowled Wickets":0, "Economy":0, "Wides":0, "No Balls":0, "Catches":0, "Direct Throw Runout":0, "Runout involving Thrower and Catcher":0 }
            names = []
            names.append(dnb_batsman_name)
            splitted_name = dnb_batsman_name.split()
            if len(splitted_name)>1:
                new_name = splitted_name[0][0]+" "+splitted_name[-1]
                names.append(new_name)
                new_name = splitted_name[-1]
                names.append(new_name)
            alternate_names.append(names)
            player_stats[dnb_batsman_name] = stats

    # Get Second Innings Batting details
    rows = table_body[2].find_all('tr')
    for row in rows[::2]:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        if cols[0] == 'Extras':
            continue
        else:
            stats = {"Runs Scored":0, "Balls Faced":0, "Fours":0, "Sixes":0, "Strike Rate":0, "Dismissal":"Did Not Bat", "Overs Bowled":0, "Maidens":0, "Runs Conceded":0, "Wickets":0, "LBW/Bowled Wickets":0, "Economy":0, "Wides":0, "No Balls":0, "Catches":0, "Direct Throw Runout":0, "Runout involving Thrower and Catcher":0 }
            name = re.sub(r"\W+", ' ', cols[0].split("(c)")[0]).strip()
            names = []
            names.append(name)
            splitted_name = name.split()
            if len(splitted_name)>1:
                new_name = splitted_name[0][0]+" "+splitted_name[-1]
                names.append(new_name)
                new_name = splitted_name[-1]
                names.append(new_name)
            alternate_names.append(names)
            stats["Runs Scored"] = int(cols[2])
            stats["Balls Faced"] = int(cols[3])
            stats["Fours"] = int(cols[5])
            stats["Sixes"] = int(cols[6])
            stats["Strike Rate"] = float(cols[7])
            stats["Dismissal"] = cols[1].replace("†","")
            player_stats[name] = stats
    
    # Getting players which didn't bat
    dnb_row = bs.find_all("tfoot")[1].find_all("div")
    for c in [dnb_row[0]]:
        if str(c).find("Fall of wickets")!=-1:
            break
        dnb_cols = c.find_all('span')
        dnb = [x.text.strip().split("(c)")[0] for x in dnb_cols]
        dnb = filter(lambda item: item, [re.sub(r"\W+", ' ', x).strip() for x in dnb])
        for dnb_batsman_name in dnb:
            stats = {"Runs Scored":0, "Balls Faced":0, "Fours":0, "Sixes":0, "Strike Rate":0, "Dismissal":"Did Not Bat", "Overs Bowled":0, "Maidens":0, "Runs Conceded":0, "Wickets":0, "LBW/Bowled Wickets":0, "Economy":0, "Wides":0, "No Balls":0, "Catches":0, "Direct Throw Runout":0, "Runout involving Thrower and Catcher":0 }
            names = []
            names.append(dnb_batsman_name)
            splitted_name = dnb_batsman_name.split()
            if len(splitted_name)>1:
                new_name = splitted_name[0][0]+" "+splitted_name[-1]
                names.append(new_name)
                new_name = splitted_name[-1]
                names.append(new_name)
            alternate_names.append(names)
            player_stats[dnb_batsman_name] = stats

    # Get First Innings Bowling details
    rows = table_body[1].find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        name = re.sub(r"\W+", ' ', cols[0].split("(c)")[0]).strip()
        player_stats[name]["Overs Bowled"] = float(cols[1])
        player_stats[name]["Maidens"] = int(cols[2])
        player_stats[name]["Runs Conceded"] = int(cols[3])
        player_stats[name]["Wickets"] = int(cols[4])
        player_stats[name]["Economy"] = float(cols[5])
        player_stats[name]["Wides"] = int(cols[9])
        player_stats[name]["No Balls"] = int(cols[10])
    
    # Get Second Innings Bowling details
    rows = table_body[3].find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        name = re.sub(r"\W+", ' ', cols[0].split("(c)")[0]).strip()
        player_stats[name]["Overs Bowled"] = float(cols[1])
        player_stats[name]["Maidens"] = int(cols[2])
        player_stats[name]["Runs Conceded"] = int(cols[3])
        player_stats[name]["Wickets"] = int(cols[4])
        player_stats[name]["Economy"] = float(cols[5])
        player_stats[name]["Wides"] = int(cols[9])
        player_stats[name]["No Balls"] = int(cols[10])
    
    # Getting catches and LBW/Bowled stats
    for stat in player_stats.values():
        dismissal = stat["Dismissal"]
        if dismissal.find("c & b ") == 0:
            catcher = dismissal.split("c & b ")[1]
            name = get_primary_name(alternate_names,catcher)
            player_stats[name]["Catches"]+=1
        elif dismissal.find("c ") == 0:
            if dismissal.find("sub (")!=-1:
                continue
            catcher = dismissal.split("c ")[1].split(" b ")[0]
            name = get_primary_name(alternate_names,catcher)
            player_stats[name]["Catches"]+=1
        elif dismissal.find("st ") == 0:
            if dismissal.find("sub (")!=-1:
                continue
            direct_thrower = dismissal.split("st ")[1].split(" b ")[0]
            name = get_primary_name(alternate_names,direct_thrower)
            player_stats[name]["Direct Throw Runout"]+=1
        elif dismissal.find("run out (")==0:
            string = dismissal[9:-1]
            string_list = string.split("/")
            if len(string_list)==1:
                if string_list[0].find("sub (")!=-1:
                    continue
                name = get_primary_name(alternate_names,string_list[0])
                player_stats[name]["Direct Throw Runout"]+=1
            else:
                for item in string_list:
                    if item.find("sub (")!=-1:
                        continue
                    name = get_primary_name(alternate_names,item)
                    player_stats[name]["Runout involving Thrower and Catcher"]+=1
        elif dismissal.find("lbw")==0:
            bowler = dismissal.split("lbw b ")[1]
            name = get_primary_name(alternate_names,bowler)
            player_stats[name]["LBW/Bowled Wickets"]+=1
        elif dismissal.find("b")==0:
            bowler = dismissal.split("b ")[1]
            name = get_primary_name(alternate_names,bowler)
            player_stats[name]["LBW/Bowled Wickets"]+=1
    return player_stats
        

                



