"""Zach Sampson"""
import random

class Batter:
    def __init__(self, name, contact, power, speed, fielding):
        self.name = name
        self.contact = contact
        self.power = power
        self.speed = speed
        self.fielding = fielding
    
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

def at_bat(pitcher, batter):
    """Simulates a single at-bat requiring one pitcher object and one batter object"""
    base_walk_proportion = 0.098
    walk_proportion = base_walk_proportion - pitcher.control * 0.0003
    random_walk_prop = random.random()
    if walk_proportion >= random_walk_prop:
        result = Result("Walk")
        return result
    else:
        base_stikeout_prop = 0.21
        strikout_prop = 0.0003 * (pitcher.stuff + pitcher.velocity - batter.contact) + base_stikeout_prop
        random_strikeout_prop = random.random()
        if strikout_prop >= random_strikeout_prop:
            result = Result("Strikeout")
            return result
        else:
            base_hit_prop = 0.335
            hit_prop = 0.001 * (batter.contact - pitcher.stuff) + base_hit_prop
            random_hit_prop = random.random()
            if hit_prop >= random_hit_prop:
                hit_random = random.random()
                hr_base_prop = 0.03
                hr_prop = batter.power * 0.001 + hr_base_prop
                double_base_prop = 0.15
                double_prop = batter.power * 0.0003 + double_base_prop
                double_threshold = double_prop + hr_prop
                if hr_prop >= hit_random:
                    result = Result("Homerun")
                    return result
                elif double_threshold >= hit_random:
                    result = Result("Double")
                    return result
                else:
                    result = Result("Single")
                    return result
            else:
                error_base_prop = 0.014
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
    home_runs = 0
    errors = 0
    bases = [None, None, None]
    i = batter_index

    while outs < 3:
        result = at_bat(pitcher, lineup[i])
        if result.result == "Out" or result.result == "Strikeout" :
            if result.result == "Out":
                print(lineup[i].name + " hits into an out")
            else:
                strikeouts += 1
                print(pitcher.name + " strikes out " + lineup[i].name + "!")
            outs += 1
        elif result.result == "Homerun" or result.result == "Double" or result.result == "Single":
            hits += 1
            if result.result == "Homerun":
                bases, runs = advance_runners(result.result, bases, lineup[i], runs)
                home_runs += 1
                print(lineup[i].name + " hits it out of the park, HOMERUN!!")
            elif result.result == "Double":
                bases, runs = advance_runners(result.result, bases, lineup[i], runs)
                doubles += 1
                print(lineup[i].name + " hits it for a double.")
            elif result.result == "Single":
                bases, runs = advance_runners(result.result, bases, lineup[i], runs)
                singles += 1
                print(lineup[i].name + " hits it for a single.")
        elif result.result == "Walk":
            bases, runs = advance_runners(result.result, bases, lineup[i], runs)
            walks += 1
            print(lineup[i].name + " draws a walk.")
        elif result.result == "Error":
            bases, runs = advance_runners(result.result, bases, lineup[i], runs)
            errors += 1
            print(lineup[i].name + " gets on base from an error.")
        i += 1
        if i >= len(lineup):
            i = 0

    print("Strikeouts: " + str(strikeouts), "Runs: " + str(runs), "Walks: " + str(walks), "Hits: " + str(hits),
        "Singles: " + str(singles), "Doubles: " + str(doubles), "Home Runs: " + str(home_runs), "Errors: " + str(errors))
    return {"runs": runs, "strikeouts": strikeouts, "walks": walks, "hits": hits, "singles": singles, "doubles": doubles,
            "home_runs": home_runs, "errors": errors, "next_batter_index": i}

def advance_runners(result, bases, batter, runs):
    first_base = bases[0]
    second_base = bases[1]
    third_base = bases[2]
    if result == "Single" or result == "Error":
        if third_base:
            runs += 1
            third_base = None
        if second_base:
            third_base = second_base
            second_base = None
        if first_base:
            second_base = first_base
            first_base = None
        first_base = batter
    elif result == "Double":
        if third_base:
            runs += 1
            third_base = None
        if second_base:
            runs += 1
            second_base = None
        if first_base:
            third_base = first_base
            first_base = None
        second_base = batter
    elif result == "Triple":
        if third_base:
            runs += 1
            third_base = None
        if second_base:
            second_base = None
            runs += 1
        if first_base:
            first_base = None
            runs += 1
        third_base = batter
    elif result == "Homerun":
        if third_base:
            runs += 1
            third_base = None
        if second_base:
            second_base = None
            runs += 1
        if first_base:
            first_base = None
            runs += 1
        runs += 1
    elif result == "Walk":
        if first_base and second_base and third_base:
            third_base = None
            runs += 1
        if first_base and second_base:
            third_base = second_base
            second_base = None
        if first_base:
            second_base = first_base
            first_base = None
        first_base = batter
    new_bases = [first_base, second_base, third_base]
    return new_bases, runs
