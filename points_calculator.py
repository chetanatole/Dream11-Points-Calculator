from scrapper import get_playerstats

# Dream11 T20 Points System
T20_points = {
    "announced" : 4,
    "run" : 1,
    "boundary_bonus" : 1,
    "six_bonus" : 2,
    "30_run_bonus" : 4,
    "half_century_bonus" : 8,
    "century_bonus" : 16,
    "dismissal_for_duck" : -2,
    "wicket" : 25,
    "lbw/bowled_bonus" : 8,
    "3_wicket_haul" : 4,
    "4_wicket_haul" : 8,
    "5_wicket_haul" : 16,
    "maiden" : 12,
    "catch" : 8,
    "3_catch_bonus" : 4,
    "runout(DirectHit/Stumping)" : 12,
    "runout(Catcher/Thrower)" : 6,
    "min_overs_to_be_bowled_for_economy_points" : 2,
    "economy_points" : {
        "<5" : 6,
        ">=5 and <=5.99" : 4,
        ">=6 and <=7" : 2,
        ">=10 and <=11" : -2,
        ">=11.01 and <=12" : -4,
        ">12" : -6 
    },
    "min_balls_to_be_played_for_strikerate_points" : 10,
    "strike_rate_points" : {
        ">170" : 6,
        ">=150.01 and <=170" : 4,
        ">=130 and <=150" : 2,
        ">=60 and <=70" : -2,
        ">=50 and <=59.99" : -4,
        "<50" : -6
    }
}

# Dream11 ODI Points System 
ODI_points = {
    "announced" : 4,
    "run" : 1,
    "boundary_bonus" : 1,
    "six_bonus" : 2,
    "half_century_bonus" : 4,
    "century_bonus" : 8,
    "dismissal_for_duck" : -3,
    "wicket" : 25,
    "lbw/bowled_bonus" : 8,
    "4_wicket_haul" : 4,
    "5_wicket_haul" : 8,
    "maiden" : 4,
    "catch" : 8,
    "3_catch_bonus" : 4,
    "runout(DirectHit/Stumping)" : 12,
    "runout(Catcher/Thrower)" : 6,
    "min_overs_to_be_bowled_for_economy_points" : 5,
    "economy_points" : {
        "<2.5" : 6,
        ">=2.5 and <=3.49" : 4,
        ">=3.5 and <=4.5" : 2,
        ">=7 and <=8" : -2,
        ">=8.01 and <=9" : -4,
        ">9" : -6 
    },
    "min_balls_to_be_played_for_strikerate_points" : 20,
    "strike_rate_points" : {
        ">140" : 6,
        ">=120.01 and <=140" : 4,
        ">=100 and <=120" : 2,
        ">=40 and <=50" : -2,
        ">=30 and <=39.99" : -4,
        "<30" : -6
    }
}

def calculate_t20_points(playerstats):
    player_list = []
    for player,stats in playerstats.items():
        points = 0
        points += T20_points["announced"]
        points += stats["Runs Scored"]*T20_points["run"]
        points += stats["Fours"]*T20_points["boundary_bonus"]
        points += stats["Sixes"]*T20_points["six_bonus"]
        if stats["Runs Scored"]>=100:
            points += T20_points["century_bonus"]
        elif stats["Runs Scored"]>=50:
            points += T20_points["half_century_bonus"]
        elif stats["Runs Scored"]>=30:
            points += T20_points["30_run_bonus"]
        if stats["Dismissal"]!="Did Not Bat" and stats["Dismissal"]!="not out":
            if stats["Runs Scored"] == 0:
                points += T20_points["dismissal_for_duck"]
        points += stats["Wickets"]*T20_points["wicket"]
        points += stats["LBW/Bowled Wickets"]*T20_points["lbw/bowled_bonus"]
        if stats["Wickets"]>=5:
            points += T20_points["5_wicket_haul"]
        elif stats["Wickets"]==4:
            points += T20_points["4_wicket_haul"]
        elif stats["Wickets"]==3:
            points += T20_points["3_wicket_haul"]
        points += stats["Maidens"]*T20_points["maiden"]
        points += stats["Catches"]*T20_points["catch"]
        if stats["Catches"]>=3:
            points += T20_points["3_catch_bonus"]
        points += stats["Direct Throw Runout"]*T20_points["runout(DirectHit/Stumping)"]
        points += stats["Runout involving Thrower and Catcher"]*T20_points["runout(Catcher/Thrower)"]
        if stats["Overs Bowled"]>=T20_points["min_overs_to_be_bowled_for_economy_points"]:
            eco = stats["Economy"]
            for x,y in T20_points["economy_points"].items():
                l = x.split(" and ")
                if len(l)==1:
                    if eval(str(eco)+l[0]):
                        points += y
                        break
                else:
                    if eval(str(eco)+l[0]) and eval(str(eco)+l[1]):
                        points += y
                        break
        if stats["Balls Faced"]>=T20_points["min_balls_to_be_played_for_strikerate_points"]:
            str_rate = stats["Strike Rate"]
            for x,y in T20_points["strike_rate_points"].items():
                l = x.split(" and ")
                if len(l)==1:
                    if eval(str(str_rate)+l[0]):
                        points += y
                        break
                else:
                    if eval(str(str_rate)+l[0]) and eval(str(str_rate)+l[1]):
                        points += y
                        break
        player_list.append([player,points])
        player_list = sorted(player_list, key = lambda x: x[1],reverse=True)
    return player_list

def calculate_ODI_points(playerstats):
    player_list = []
    for player,stats in playerstats.items():
        points = 0
        points += ODI_points["announced"]
        points += stats["Runs Scored"]*ODI_points["run"]
        points += stats["Fours"]*ODI_points["boundary_bonus"]
        points += stats["Sixes"]*ODI_points["six_bonus"]
        if stats["Runs Scored"]>=100:
            points += ODI_points["century_bonus"]
        elif stats["Runs Scored"]>=50:
            points += ODI_points["half_century_bonus"]
        if stats["Dismissal"]!="Did Not Bat" and stats["Dismissal"]!="not out":
            if stats["Runs Scored"] == 0:
                points += ODI_points["dismissal_for_duck"]
        points += stats["Wickets"]*ODI_points["wicket"]
        points += stats["LBW/Bowled Wickets"]*ODI_points["lbw/bowled_bonus"]
        if stats["Wickets"]>=5:
            points += ODI_points["5_wicket_haul"]
        elif stats["Wickets"]==4:
            points += ODI_points["4_wicket_haul"]
        points += stats["Maidens"]*ODI_points["maiden"]
        points += stats["Catches"]*ODI_points["catch"]
        if stats["Catches"]>=3:
            points += ODI_points["3_catch_bonus"]
        points += stats["Direct Throw Runout"]*ODI_points["runout(DirectHit/Stumping)"]
        points += stats["Runout involving Thrower and Catcher"]*ODI_points["runout(Catcher/Thrower)"]
        if stats["Overs Bowled"]>=ODI_points["min_overs_to_be_bowled_for_economy_points"]:
            eco = stats["Economy"]
            for x,y in ODI_points["economy_points"].items():
                l = x.split(" and ")
                if len(l)==1:
                    if eval(str(eco)+l[0]):
                        points += y
                        break
                else:
                    if eval(str(eco)+l[0]) and eval(str(eco)+l[1]):
                        points += y
                        break
        if stats["Balls Faced"]>=ODI_points["min_balls_to_be_played_for_strikerate_points"]:
            str_rate = stats["Strike Rate"]
            for x,y in ODI_points["strike_rate_points"].items():
                l = x.split(" and ")
                if len(l)==1:
                    if eval(str(str_rate)+l[0]):
                        points += y
                        break
                else:
                    if eval(str(str_rate)+l[0]) and eval(str(str_rate)+l[1]):
                        points += y
                        break
        player_list.append([player,points])
        player_list = sorted(player_list, key = lambda x: x[1],reverse=True)
    return player_list

if __name__=="__main__":
    print("Select Type of Match\n1.T20\n2.One Day")
    type = int(input())
    print("Enter ESPN Cricinfo scorecard link : ")
    url = input()
    playerstats = get_playerstats(url)
    if type == 1:
        player_list = calculate_t20_points(playerstats)
    elif type == 2:
        player_list = calculate_ODI_points(playerstats)
    col_width = max(len(str(word)) for row in player_list for word in row) + 2  # padding
    for row in player_list:
        print("".join(str(word).ljust(col_width) for word in row))

            
            