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
pitcher1 = Pitcher("Luke Sampson", 99, 99, 99)

def at_bat(pitcher, batter):
    """Simulates a single at-bat requiring one pitcher object and one batter object"""
    base_walk_proportion = 0.098
    walk_proportion = base_walk_proportion - pitcher.control * 0.0003
    random_walk_prop = random.random()
    if(walk_proportion >= random_walk_prop):
        result = Result("Walk")
        return result
    else:
        base_stikeout_prop = 0.21
        strikout_prop = 0.0003 * (pitcher.stuff + pitcher.velocity - batter.contact) + base_stikeout_prop
        random_strikeout_prop = random.random()
        if(strikout_prop >= random_strikeout_prop):
            result = Result("Strikeout")
            return result
        else:
            base_hit_prop = 0.335
            hit_prop = 0.001 * (batter.contact - pitcher.stuff) + base_hit_prop
            random_hit_prop = random.random()
            if(hit_prop >= random_hit_prop):
                hit_random = random.random()
                hr_base_prop = 0.03
                hr_prop = batter.power * 0.001 + hr_base_prop
                double_base_prop = 0.15
                double_prop = batter.power * 0.0003 + double_base_prop
                double_threshold = double_prop + hr_prop
                if(hr_prop >= hit_random):
                    result = Result("Homerun")
                    return result
                elif(double_threshold >= hit_random):
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