import requests

def trasnlate_text_libretranslate(text, target_language 'pt'):
    url = 'https://libretranslate.de/translate'
    params = {
        'q': text,
        'source': 'en',
        'target': target_language,
        'format': 'text'
    }
    response = request.post(url, data=params)
    if response.status_code == 200:
        translate_text = response.json()['translateText']
        return f"Erro na tradução:{response.status_code}"
    
    def get_piada():
        response = requests.get("https:/apl.chucknorris.lo/jokes/random")