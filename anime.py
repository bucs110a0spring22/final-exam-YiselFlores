import requests
import json
import random
from funcy import join

class Anime():
  def __init__(self, name):
        self.url = f'https://animechan.vercel.app/api/quotes/character?name={name}'
       
  
  def get_info(self):
        ''' 
        gets anime qoute based on character's anime.
        Takes no parameters. Returns a string
        '''
        r = requests.get(self.url)
        self.response = r.json()
        join(self.response)
        #print(self.response)
        values_of_key = [a_dict["quote"] for a_dict in self.response]
        for i in values_of_key:
          
         return random.choice(values_of_key)
        
  def anime_name(self):
    get_name = [a_dict["anime"] for a_dict in self.response]
    #print(get_name)
    ''' 
    gets anime name based on character's name and formats the name.
    Takes no parameters. Returns a string
    '''
    a_name = get_name[0]
    #print(a_name)
    if a_name == "Naruto Shippuuden":
     a_name = "naruto"
    elif a_name == 'Shingeki no Kyojin':
      a_name = "attack_on_titan"
    elif a_name == 'Dragon Ball Z':
      a_name = "dragon_ball"
    elif a_name == 'Fullmetal Alchemist: Brotherhood':
      a_name = "fma_brotherhood" 
    elif a_name == 'Gekijōban Gintama Kanketsu-hen: Yorozuya yo Eien Nare':
      a_name = "gintama"
   # print(type(a_name))
    a_name  = a_name.replace(" ","_")
    a_name = a_name.lower()
    
   # print(a_name)
    return a_name

