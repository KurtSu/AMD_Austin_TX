'''
Coding excrcises written for the position of 
https://jobs.amd.com/job/Austin-Software-Development-Engineer-1-Texa/853677600/
author: Tianwen Su
'''

''' task 1, binary recursive max.
args:
    arr: an non-empty list of integars.

returns:
    the max value of arr
'''
def max(arr):
    l = len(arr)
    if l == 0:
        print('Input should have at least 1 element.')
        return 
    
    # base cases
    if l == 1:
        return arr[0]

    # recursive step
    else:
        mid = l // 2
        a = max(arr[: mid])
        b = max(arr[mid: ])
        return a if a > b else b

''' task 2, JSON processing. If the input is
    a dictionary, call this.
args:
    json_obj: a dictionary contains key 'superheros',
    which value is a list of dictionaries.

returns:
    a dictionary contains key 'superherosbyCity', 
    which value is a list of dictionaries.
'''
def json_transformation(json_obj):
    superhero_lst = json_obj['superheros']
    city_heros = {}
    
    for id in superhero_lst:
        city = id['city']
        hero = id['name']
        if city in city_heros:
            city_heros[city].append(hero)
        else:
            city_heros[city] = [hero]

    city_lst = []
    for city in city_heros:
        city_lst.append({city: city_heros[city]})
        
    return {'superherosbyCity': city_lst}


''' task2: JSON processing, a shell of
    json_transformation。 If the input is
    a JSON string, call this one.
args:
    json_str: a JSON string.
'''
def json_str_transformation(json_str):
    import json
    json_obj = json.loads(json_str)
    return json_transformation(json_obj)

''' task 3, recursive string processing.
args:
    s: a string

returns:
    a list of 2-tuples.
'''
def str_squeezing(s):
    l = len(s)
    
    # base cases
    if l == 0:
        return []
    elif l == 1:
        return [(s[0], )]
        
    # recursive step
    else:
        return [(s[0], s[-1])] + str_squeezing(s[1: -1])
