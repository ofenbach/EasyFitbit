import os
from requests_oauthlib import OAuth2Session


class FitbitClient:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.oauth = None

        self.authorization_base_url = 'https://www.fitbit.com/oauth2/authorize'
        self.token_url = 'https://api.fitbit.com/oauth2/token'
        self.scope = ["activity", "nutrition", "heartrate", "location", "profile", "settings", "sleep", "social",
                      "weight"]

    def authenticate(self):
        self.oauth = OAuth2Session(self.client_id, scope=self.scope, redirect_uri=self.redirect_uri)

        authorization_url, state = self.oauth.authorization_url(self.authorization_base_url)
        print('Please go to the following URL and authorize the app:\n' + authorization_url)

        redirect_response = input('Paste the full redirect URL here:')
        self.oauth.fetch_token(self.token_url, authorization_response=redirect_response,
                               client_secret=self.client_secret)

    def get_profile(self):
        response = self.oauth.get('https://api.fitbit.com/1/user/-/profile.json')
        return response.json()

    def get_heart_rate(self, date='today', period='1d'):
        response = self.oauth.get(f'https://api.fitbit.com/1/user/-/activities/heart/date/{date}/{period}.json')
        return response.json()

    def get_activities(self, date='today'):
        response = self.oauth.get(f'https://api.fitbit.com/1/user/-/activities/date/{date}.json')
        return response.json()

    def get_sleep(self, date='today'):
        response = self.oauth.get(f'https://api.fitbit.com/1.2/user/-/sleep/date/{date}.json')
        return response.json()

    def get_body(self, date='today'):
        response = self.oauth.get(f'https://api.fitbit.com/1/user/-/body/date/{date}.json')
        return response.json()

    def get_nutrition(self, date='today'):
        response = self.oauth.get(f'https://api.fitbit.com/1/user/-/foods/log/date/{date}.json')
        return response.json()

    def get_devices(self):
        response = self.oauth.get('https://api.fitbit.com/1/user/-/devices.json')
        return response.json()

    def get_hrv(self, date='2023-05-19', raw_json=False):
        response = self.oauth.get(f'https://api.fitbit.com/1/user/-/hrv/date/{date}.json')
        json_data = response.json()

        if raw_json:
            return json_data

        daily_rmssd = json_data['hrv'][0]['value']['dailyRmssd']
        return daily_rmssd


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://127.0.0.1:8080/'     # this is a default value, change to your needs

fitbit = FitbitClient(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
fitbit.authenticate()
print(fitbit.get_profile())
print(fitbit.get_heart_rate())
print(fitbit.get_hrv())
print(fitbit.get_hrv(raw_json=True))
print(fitbit.get_devices())
