import requests
import json
from PIL import Image

# Looking for a image of a pokemon
def image(response):
    # Take the image url from JSON
    sprites = response.json()['sprites']['front_default']

    # Configuring image
    image = Image.open(requests.get(sprites, stream=True).raw)

    # print pokemon image
    print(image,'\n')

# Looking for a pokemons type
def unique_type(response):
    # Creating a variable to work with
    types = response.json()['types']

    print('The type(s) of', response.json()['forms'][0]['name'], 'is:')

    # Print the pokemon's type
    for i in range(len(types)):
        print('-', types[i]['type']['name'])

# Consulting API types
def cause_double_damage(response):
    # Creating a variable to work with JSON
    types = response.json()['damage_relations']

    print('The type(s) of', response.json()['name'], 'cause double damage is:' )

    # Loop telling the type with causes double damage
    for i in range(len(types['double_damage_to']) - 1):
        print('-', types['double_damage_to'][i]['name'])

def receive_double_damage(response):
    # Creating a variable to work with JSON
    types = response.json()['damage_relations']

    print('The type(s) of', response.json()['name'], 'receive double damage is:' )

    # Loop telling the type with receives double damage
    for i in range(len(types['double_damage_from']) - 1):
        print('-', types['double_damage_from'][i]['name'])

def pokemon_ability(response):
    # Creating a variable to work with JSON
    ability = response.json()['pokemon']

    print('The type(s) of', response.json()['name'], 'receive double damage is:' )

    # Loop telling the type with receives double damage
    for i in range(len(ability) - 1):
        print('-', ability[i]['pokemon']['name'])