import requests
import anime
from anime import Anime
import anime_facts

def main():
  anime_character = input("Enter an animes character's name to get a random quote from the character and a fact from the anime! \n CHOOSE FROM: Naruto, Bleach, Hunter X Hunter, One Piece, Dragon Ball Z, Attack On Titan, Gintama, Boku no Hero Academia \n \n  ")
 #print(anime_character)
  results = anime.Anime(anime_character)
   
  print(results.get_info() + "\n")
  #print(results.anime_name())
  
  facts_results = anime_facts.Anime_facts(results.anime_name())
  print(facts_results.get_info()+ "\n")

main()