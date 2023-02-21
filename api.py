import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/characters')
def get_characters():
    url = 'https://gateway.marvel.com/v1/public/characters'
    params = {
        'apikey': '029f358ccddef4f174d590c60aaad4d6',
        'ts': '1',
        'hash': '399481354b04138440c5e140786c1f85'
    }

    response = requests.get(url, params=params).json()

    characters = []

    for character in response['data']['results']:
        name = character['name']
        description = character['description']
        thumbnail = character['thumbnail']['path'] + '.' + character['thumbnail']['extension']

        characters.append({
            'name': name,
            'description': description,
            'thumbnail': thumbnail
        })

    return jsonify(characters)

if __name__ == '__main__':
    app.run()
