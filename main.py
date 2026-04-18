"""Zach Sampson"""
import random

class Batter:
    def __init__(self, name, contact, power, speed, fielding):
        self.name = name
        self.contact = contact
        self.power = power
        self.speed = speed
        self.fielding = fielding

        self.games_played = 0
        self.at_bats = 0
        self.hits = 0
        self.singles = 0
        self.doubles = 0
        self.triples = 0
        self.hrs = 0
        self.walks = 0
        self.strikeouts = 0
        self.runs = 0
        self.rbi = 0
    
class Pitcher:
    def __init__(self, name, velocity, control, stuff):
        self.name = name
        self.velocity = velocity
        self.control = control
        self.stuff = stuff

class Result:
    def __init__(self, result):
        self.result = result

batter1 = Batter("Zach Sampson", 50, 50, 50, 50)
batter2 = Batter("Negro Destroyer", 70, 30, 45, 80)
batter3 = Batter("Mike Trout", 95, 85, 85, 80)
batter4 = Batter("Ronald Acuna Jr.", 50, 50, 50, 50)
batter5 = Batter("Matt Olson", 70, 30, 45, 80)
batter6 = Batter("Aaron Judge", 95, 85, 85, 80)
batter7 = Batter("Austin Riley", 50, 50, 50, 50)
batter8 = Batter("Yordan Alvarez", 70, 30, 45, 80)
batter9 = Batter("Michael Harris II", 95, 85, 85, 80)
batter_lineup = [batter1, batter2, batter3, batter4, batter5, batter6, batter7, batter8, batter9]
pitcher1 = Pitcher("Luke Sampson", 70, 70, 70)
team1 = {"lineup": batter_lineup, "pitcher": pitcher1}

away_batter1 = Batter("Jim Bob", 70, 85, 60, 80)
away_batter2 = Batter("Slim Jim", 90, 70, 85, 50)
away_batter3 = Batter("Blackbeard Joe", 70, 99, 30, 80)
away_batter4 = Batter("Jim Crow", 70, 85, 60, 80)
away_batter5 = Batter("Mommy Milk", 70, 85, 60, 80)
away_batter6 = Batter("Walter White", 70, 85, 60, 80)
away_batter7 = Batter("Tony Stark", 70, 85, 60, 80)
away_batter8 = Batter("Crew Crawdad", 70, 85, 60, 80)
away_batter9 = Batter("Coach Rac", 70, 85, 60, 80)
away_batting_lineup = [away_batter1, away_batter2, away_batter3, away_batter4, away_batter5, away_batter6, away_batter7, away_batter8, away_batter9]
away_pitcher1 = Pitcher("Nolan Ryan", 80, 60, 70)
team2 = {"lineup":away_batting_lineup, "pitcher": away_pitcher1}

def at_bat(pitcher, batter):
    """Simulates a single at-bat requiring one pitcher object and one batter object"""
    base_walk_proportion = 0.12
    walk_proportion = base_walk_proportion - pitcher.control * 0.00025
    random_walk_prop = random.random()
    if walk_proportion >= random_walk_prop:
        result = Result("Walk")
        return result
    else:
        base_stikeout_prop = 0.21
        strikout_prop = 0.0002 * (pitcher.stuff + pitcher.velocity - batter.contact) + base_stikeout_prop
        random_strikeout_prop = random.random()
        if strikout_prop >= random_strikeout_prop:
            result = Result("Strikeout")
            return result
        else:
            base_hit_prop = 0.315
            hit_prop = 0.001 * (batter.contact - pitcher.stuff) + base_hit_prop
            random_hit_prop = random.random()
            if hit_prop >= random_hit_prop:
                hit_random = random.random()
                hr_base_prop = 0.015
                hr_prop = batter.power * 0.001 + hr_base_prop
                double_base_prop = 0.155
                double_prop = batter.power * 0.0003 + double_base_prop
                double_threshold = double_prop + hr_prop
                triple_base_prop = 0.008
                triple_prop = batter.speed * 0.001 + triple_base_prop
                triple_threshold = double_threshold + triple_prop
                if hr_prop >= hit_random:
                    result = Result("Homerun")
                    return result
                elif double_threshold >= hit_random:
                    result = Result("Double")
                    return result
                elif triple_threshold >= hit_random:
                    result = Result("Triple")
                    return result
                else:
                    result = Result("Single")
                    return result
            else:
                error_base_prop = 0.035
                random_error_prop = random.random()
                if(error_base_prop >= random_error_prop):
                    result = Result("Error")
                    return result
                else:
                    result = Result("Out")
                    return result

def simulate_inning(pitcher, lineup, batter_index):
    outs = 0
    strikeouts = 0
    runs = 0
    hits = 0
    walks = 0
    singles = 0
    doubles = 0
    triples = 0
    home_runs = 0
    errors = 0
    bases = [None, None, None]
    i = batter_index

    while outs < 3:
        result = at_bat(pitcher, lineup[i])
        if result.result == "Out" or result.result == "Strikeout" :
            if result.result == "Out":
                #print(lineup[i].name + " hits into an out")
                outs+=1
            else:
                strikeouts += 1
                outs+=1
                #print(pitcher.name + " strikes out " + lineup[i].name + "!")
            #outs += 1
        elif result.result == "Homerun" or result.result == "Triple" or result.result == "Double" or result.result == "Single":
            hits += 1
            if result.result == "Homerun":
                bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
                home_runs += 1
                #print(lineup[i].name + " hits it out of the park, HOMERUN!!")
            elif result.result == "Triple":
                bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
                triples += 1
                #print(lineup[i].name + " hits it for a triple.")
            elif result.result == "Double":
                bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
                doubles += 1
                #print(lineup[i].name + " hits it for a double.")
            elif result.result == "Single":
                bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
                singles += 1
                #print(lineup[i].name + " hits it for a single.")
        elif result.result == "Walk":
            bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
            walks += 1
            #print(lineup[i].name + " draws a walk.")
        elif result.result == "Error":
            bases, runs, runs_in_one_play = advance_runners(result.result, bases, lineup[i], runs)
            errors += 1
            #print(lineup[i].name + " gets on base from an error.")
        update_stats(lineup[i], result.result, runs_in_one_play)
        i += 1
        if i >= len(lineup):
            i = 0

    #print("Strikeouts: " + str(strikeouts), "Runs: " + str(runs), "Walks: " + str(walks), "Hits: " + str(hits),
        #"Singles: " + str(singles), "Doubles: " + str(doubles), "Triples: " + str(triples), "Home Runs: " + str(home_runs), "Errors: " + str(errors))
    return {"runs": runs, "strikeouts": strikeouts, "walks": walks, "hits": hits, "singles": singles, "doubles": doubles, 
            "triples": triples, "home_runs": home_runs, "errors": errors, "next_batter_index": i}

def advance_runners(result, bases, batter, runs):
    first_base = bases[0]
    second_base = bases[1]
    third_base = bases[2]
    additional_runs = 0
    if result == "Error":
        base_error_speed_prop = 0.4
        error_speed_prop = 0.001 * batter.speed + base_error_speed_prop
        random_error_speed = random.random()
        if third_base:
            additional_runs += 1
            third_base.runs += 1
            third_base = None
        if second_base:
            if error_speed_prop > random_error_speed:
                additional_runs += 1
                second_base.runs += 1
                second_base = None
            else:
                third_base = second_base
                second_base = None
        if first_base:
            if error_speed_prop > random_error_speed:
                third_base = first_base
                first_base = None
            else:
                second_base = first_base
                first_base = None
        first_base = batter
    elif result == "Single":
        base_single_speed_prop = 0.71
        single_speed_prop = 0.0013 * batter.speed + base_single_speed_prop
        random_single_speed_prop = random.random()
        if third_base:
            additional_runs += 1
            third_base.runs += 1
            third_base = None
        if second_base:
            if single_speed_prop > random_single_speed_prop:
                additional_runs += 1
                second_base.runs += 1
                second_base = None
            else:
                third_base = second_base
                second_base = None
        if first_base:
            if single_speed_prop > random_single_speed_prop:
                third_base = first_base
                first_base = None
            else: 
                second_base = first_base
                first_base = None
        first_base = batter
    elif result == "Double":
        double_speed_base_prop = 0.76
        double_speed_prop = 0.0015 * batter.speed + double_speed_base_prop
        random_double_speed_prop = random.random()
        if third_base:
            additional_runs += 1
            third_base.runs += 1
            third_base = None
        if second_base:
            additional_runs += 1
            second_base.runs += 1
            second_base = None
        if first_base:
            if double_speed_prop > random_double_speed_prop:
                additional_runs += 1
                first_base.runs += 1
                first_base = None
            else: 
                third_base = first_base
                first_base = None
        second_base = batter
    elif result == "Triple":
        if third_base:
            additional_runs += 1
            third_base.runs += 1
            third_base = None
        if second_base:
            additional_runs += 1
            second_base.runs += 1
            second_base = None
        if first_base:
            additional_runs += 1
            first_base.runs += 1
            first_base = None
        third_base = batter
    elif result == "Homerun":
        if third_base:
            additional_runs += 1
            third_base.runs += 1
            third_base = None
        if second_base:
            additional_runs += 1
            second_base.runs += 1
            second_base = None
        if first_base:
            additional_runs += 1
            first_base.runs += 1
            first_base = None
        additional_runs += 1
        batter.runs += 1
    elif result == "Walk":
        if first_base and second_base and third_base:
            third_base.runs += 1
            third_base = None
            additional_runs += 1
        if first_base and second_base:
            third_base = second_base
            second_base = None
        if first_base:
            second_base = first_base
            first_base = None
        first_base = batter
    new_bases = [first_base, second_base, third_base]
    runs += additional_runs
    return new_bases, runs, additional_runs

def simulate_game(home, away):
    i = 0 # home batter index
    j = 0 # away batter index
    game_being_played = True # flag that keeps game going
    
    home_lineup = home["lineup"]
    home_pitcher = home["pitcher"]
    away_lineup = away["lineup"]
    away_pitcher = away["pitcher"]

    for i in range(len(home_lineup)):
        home_lineup[i].games_played += 1
        away_lineup[i].games_played += 1
    
    home_score = 0
    home_strikeouts = 0
    home_walks = 0
    home_hits = 0
    home_singles = 0
    home_doubles = 0
    home_triples = 0
    home_hrs = 0
    home_errors = 0
    
    away_score = 0
    away_strikeouts = 0
    away_walks = 0
    away_hits = 0
    away_singles = 0
    away_doubles = 0
    away_triples = 0
    away_hrs = 0
    away_errors = 0

    innings = 0

    while(game_being_played):
        innings += 1
        away_result = simulate_inning(home_pitcher, away_lineup, j)
        away_score += away_result["runs"]
        away_strikeouts += away_result["strikeouts"]
        away_walks += away_result["walks"]
        away_hits += away_result["hits"]
        away_singles += away_result["singles"]
        away_doubles += away_result["doubles"]
        away_triples += away_result["triples"]
        away_hrs += away_result["home_runs"]
        home_errors += away_result["errors"]
        j = away_result["next_batter_index"]

        if(innings >= 9):
            if(home_score > away_score):
                game_being_played = False
                break

        home_result = simulate_inning(away_pitcher, home_lineup, i)
        home_score += home_result["runs"]
        home_strikeouts += home_result["strikeouts"]
        home_walks += home_result["walks"]
        home_hits += home_result["hits"]
        home_singles += home_result["singles"]
        home_doubles += home_result["doubles"]
        home_triples += home_result["triples"]
        home_hrs += home_result["home_runs"]
        away_errors += home_result["errors"]
        i = home_result["next_batter_index"]

        if innings >= 9:
            if home_score != away_score:
                game_being_played = False
                break
    
    who_won = ""
    if home_score > away_score:
        who_won = "Home Team"
    elif home_score < away_score:
        who_won = "Away Team"
    #print("The game is over in " + str(innings) + " innings with a score of " + str(home_score) + "-" + str(away_score) + " favoring the " + who_won + ".")
    #print("Home Team: Runs: " + str(home_score) + " Hits: " + str(home_hits) + " Errors: " + str(home_errors))
    #print("Away Team: Runs: "+ str(away_score) + " Hits: " + str(away_hits) + " Errors: " + str(away_errors))
    return {"Total Score": home_score + away_score, "Hits": home_hits + away_hits, "HRs": home_hrs + away_hrs, "Errors": home_errors + away_errors}

def update_stats(batter, result, runs_this_play):
    if result == "Error":
        batter.at_bats += 1
    elif result == "Walk":
        batter.walks += 1
        batter.rbi += runs_this_play
    else:
        batter.at_bats += 1
        if result in ["Single", "Double", "Triple", "Homerun"]:
            batter.hits += 1
            if result == "Single":
                batter.singles += 1
            elif result == "Double":
                batter.doubles += 1
            elif result == "Triple":
                batter.triples += 1
            elif result == "Homerun":
                batter.hrs += 1
            batter.rbi += runs_this_play
        elif result == "Strikeout":
            batter.strikeouts += 1
        elif result == "Out":
            pass

def get_stats(batter):
    total_bases = batter.singles + 2*batter.doubles + 3*batter.triples + 4*batter.hrs
    if batter.at_bats == 0:
        average = 0
        slugging = 0
    else:
        average = batter.hits / batter.at_bats
        slugging =  total_bases / batter.at_bats
    if batter.walks + batter.at_bats == 0:
        on_base_percentage = 0
    else:
        on_base_percentage = (batter.walks + batter.hits) / (batter.walks + batter.at_bats)
    on_base_plus_slugging = on_base_percentage + slugging
    return {"obp": on_base_percentage, "avg": average, "tb": total_bases, "slg": slugging, "ops": on_base_plus_slugging}
