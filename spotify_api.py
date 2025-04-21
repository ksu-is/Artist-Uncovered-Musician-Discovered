import requests

client_id = '983f1e0a96244cba91205f76be50dbbd'
client_secret = '0af7fe6c6f414bf9a5ccc2de04153d93'

auth_response = requests.post('https://accounts.spotify.com/api/token', {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})

access_token = auth_response.json().get('access_token')

def search_artist(artist_name):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'q': artist_name,
        'type': 'artist'
    }
    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    data = response.json()

    if data['artists']['items']:
        return data['artists']['items'][0]['name']
    else:
        return "Artist not found"
