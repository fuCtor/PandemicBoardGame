# coding: utf-8
from .game_loader import GameLoader
from .game_script import GameScript
from configparser import ConfigParser

class IniGameLoader(GameLoader):
    def load(self, location) -> GameScript:        
        app_config = ConfigParser()
        app_config.read(location)
        script = GameScript(cities={}, diseases=set([]), connections={}, colors = [], rate = [])

        diseases_section = app_config['Diseases']
        script.diseases = set([diseases_section[id] for  id in diseases_section])

        cities_section = app_config['Cities']
        connections = app_config['Connections']
        city_colours_section = app_config['City Colours']

        script.cities = { cities_section[id]:city_colours_section[id]  for id in cities_section }
        
        script.connections = { i: [ cities_section["city" + str(n)] for n in connections[i].split()] for i in connections }

        script.colors = app_config['Colours']['colours'].split(',')

        script.initial_city = app_config['Other']['initial_city']
        script.epidemics = int(app_config['Other']['epidemics'])
        script.rate = [ int(chr) for chr in list(app_config['Other']['rate'])]
        script.cubes = int(app_config['Other']['cubes'])
        script.min_players = int(app_config['Other']['min_players'])
        script.max_players = int(app_config['Other']['max_players'])
        script.max_player_actions = int(app_config['Other']['max_player_actions'])
        script.outbreak_initial_level = int(app_config['Other']['outbreak_initial_level'])
        script.outbreak_death_level = int(app_config['Other']['outbreak_death_level'])

        return script
