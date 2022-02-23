import requests

def is_lewd_word(word: str) -> bool:
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    
    querystring = {"term": word}
    
    headers = {
        'x-rapidapi-host': "XXXXXXX",
        'x-rapidapi-key': "XXXXXXX"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)

    return bool(len(response.json()["list"]))
