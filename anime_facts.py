import requests
import json
import random
from funcy import join

class Anime_facts:
   def __init__(self,anime_name):
        self.url = f'https://anime-facts-rest-api.herokuapp.com/api/v1/{anime_name}/2'
   def get_info(self):
        ''' 
        gets anime fact based on character's respective anime.
        Takes no parameters. Returns a string
        '''
        r = requests.get(self.url)
        response = r.json()

        #print(response)
        fact=response.get('data')
        
        if fact.get('fact'):
         return fact['fact']
        else:
          return ("sorry! We dont have a quote for you :(")
       