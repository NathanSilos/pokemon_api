from functions import *

# Choose what the users wants to know
answer = input(''' Write the number above that idicates a information that you want to know:
    1 - Pokemon
    2 - Type (weakness and advantag)
    3 - Ability (pokemon that may develop this blow)

Answer: ''')

if int(answer) == 1:
    # Asking for each pokemon do you want to know about
    pokemon = input('Write the name of a Pokemon: ')
    print('\n')

    # Preparing the API to get the information
    pokemon_api = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon)

    # Getting the information from API
    response = requests.get(pokemon_api)

    # Execute functions
    image(response)
    unique_type(response)
    
    # To print the response code of a request
    #print(response.status_code)

elif int(answer) == 2:
    # Asking for each type of pokemon the user wants to know
    pokemon = input('Write the type of a Pokemon: ')

    # Preparing the API to get the information
    pokemon_api = 'https://pokeapi.co/api/v2/type/{}'.format(pokemon)

    # Getting the information from API
    response = requests.get(pokemon_api)

    # Execute funcion
    cause_double_damage(response)
    receive_double_damage(response)
elif int(answer) == 3:
    # Asking for each pokemon ability the user wants to know
    pokemon = input('Write the ability of a Pokemon: ')

    # Preparing the API to get the information
    pokemon_api = 'https://pokeapi.co/api/v2/ability/{}'.format(pokemon)

    # Getting the information from API
    response = requests.get(pokemon_api)

    # Execute function
    pokemon_ability(response)
else:
    print('Not a valid answer!!')
