from room_desc import *
import death
class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor", cc_desc)

laser_weapon_armoury = Room("Laser Weapon Armoury", lwa_desc)

the_bridge = Room("The Bridge", tb_desc)

escape_pod = Room("Escape Pod", ep_desc)

the_end_winner = Room("The End", endwin_desc)

the_end_loser = Room("The End", endlose_desc)

generic_death = Room("death", "You died.")
shoot_death = Room("death", death.shoot)
dodge_death = Room("death", death.dodge)
throw_death = Room("death", death.throw)
wrongcode_death = Room("death", death.wrongcode)
wrongpod_death = Room("death", death.wrongpod)

central_corridor.add_paths({
    'correct_answer': laser_weapon_armoury,
    'shoot': shoot_death,
    'dodge': dodge_death,
    'joke': laser_weapon_armoury
})

laser_weapon_armoury.add_paths({
    'correct_answer': the_bridge,
    '-8pi': the_bridge
})

the_bridge.add_paths({
    'correct_answer': escape_pod,
    'place bomb': escape_pod,
    'shoot!': generic_death,
    'dodge!': generic_death,
    'shoot': shoot_death,
    'dodge': dodge_death,
    'joke!': laser_weapon_armoury
})

escape_pod.add_paths({
    'correct_answer': the_end_winner,
    '2': the_end_winner,
    '*': the_end_loser,
})

START = central_corridor