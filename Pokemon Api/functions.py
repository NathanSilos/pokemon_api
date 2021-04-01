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
def type(response):

    # Creating a variable to work with
    types = response.json()['types']

    print('The type(s) of', response.json()['forms'][0]['name'], 'is:')
    # Print the pokemon's type
    for i in range(len(types)):
        print('-', types[i]['type']['name'])
