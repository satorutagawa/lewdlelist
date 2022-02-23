import requests

def is_lewd_word(word: str) -> bool:
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    
    querystring = {"term": word}
    
    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "6e2d563c40mshdde960bdc4cc32bp1cf0f3jsn6f54e76fcd31"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)

    return bool(len(response.json()["list"]))
