from functions import *


# Asking for each pokemon do you want to know about
pokemon = input('Write the name of a Pokemon: ')
print('\n')

# Preparing the API to get the information
pokemon_api = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon)

# Getting the information from API
response = requests.get(pokemon_api)

# To print the response code of a request
#print(response.status_code)

# Execute functions
image(response)
type(response)