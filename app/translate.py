import json, uuid
import requests # HTTP client
from flask_babel import _
from app import app

# Had to do a bit of my own research as the Microsoft api has changed.
# v2 was recently deprecated so I had to change the code to work with v3
def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    headers = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
         }
    url = 'https://api.cognitive.microsofttranslator.com/translate'
    params = {
            'api-version': '3.0',
            'from': source_language,
            'to': dest_language
            }    
    requestBody = [{
        'Text': text,
    }]
    payload = json.dumps(requestBody, ensure_ascii=False).encode('utf-8')

    r = requests.post(url, params=params, headers=headers, data=payload)
    if r.status_code != 200:
        print(r.status_code)
        return _('Error: the translation service failed.')
    result = json.loads(r.content.decode('utf-8-sig'))
    result = result[0]['translations'][0]['text']
    return result
