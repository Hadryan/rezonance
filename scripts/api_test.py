import requests
import json

CLIENT_ID = ""
CLIENT_SECRET = ""

AUTH_URL = "https://accounts.spotify.com/api/token"

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()


# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}



BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id = '5d2Kn9oAAh9S2EbyCo1i52,2zFF6jG5hQArbzcXz3KUWk,4JpKVNYnVcJ8tuMKjAj50A'

# actual GET request with proper header
res = requests.get("https://api.spotify.com/v1/tracks/?ids={id}".format(id = track_id), headers=headers).json()

# r_image = r["album"]["images"]
# print(res['tracks'][i]["album"]["images"][0]["url"])

for result in res["tracks"]:
    print(result["album"]["images"][0]["url"])
# print(r[0]['url'])
