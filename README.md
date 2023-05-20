# EasyFitbit
An intuitive Python wrapper for the Fitbit API, designed to simplify data retrieval and enhance the developer experience.

## Getting Started
To get started with this project, you need to first set up an application on the Fitbit developer site.

### Setting up on Fitbit Developer Site

1. Visit the [Fitbit Developer Site](https://dev.fitbit.com/)
2. Sign in with your Fitbit account (or create one if you don't have one yet).
3. Navigate to 'Manage' and then 'Register an App'.
4. Fill out the application details:
    - Application Name and Description: Choose as per your preference
    - Application Website and Organization: Optional, fill if applicable
    - OAuth 2.0 Application Type: Personal
    - Callback URL: `http://127.0.0.1:8080/` (or any other if you have a different one)
5. Once the application is registered, you'll receive a `CLIENT_ID` and `CLIENT_SECRET`. Keep these safe as you'll need them for the next steps.

### Installation

1. Clone this repository: `git clone https://github.com/<username>/<projectname>.git`
2. Navigate to the project directory: `cd <projectname>`
3. Install the required dependencies: `pip install -r requirements.txt`

### Usage

To interact with the Fitbit API using this project, follow these steps:

1. Import the FitbitClient class from the project: 
```python
from fitbit_client import FitbitClient
```

2. Instantiate a new client using your Fitbit CLIENT_ID and CLIENT_SECRET:
```python
fitbit = FitbitClient(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
```

3. Authenticate the client:
```python
fitbit.authenticate()
```

4. Now you can use the client to access Fitbit data:
```python
profile = fitbit.get_profile()
heart_rate = fitbit.get_heart_rate()
activities = fitbit.get_activities()
sleep = fitbit.get_sleep()
body = fitbit.get_body()
nutrition = fitbit.get_nutrition()
devices = fitbit.get_devices()

print("Profile: ", profile)
print("Heart rate: ", heart_rate)
print("Activities: ", activities)
print("Sleep: ", sleep)
print("Body: ", body)
print("Nutrition: ", nutrition)
print("Devices: ", devices)
```

## License
This project is licensed under the terms of the MIT license.
