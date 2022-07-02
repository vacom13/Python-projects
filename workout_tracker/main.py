import requests
import datetime

# Fill in trackapi details
API_KEYS = ''
APP_ID = ''

# Fill personal details
WEIGHT = 60.5
HEIGHT = 170
AGE = 19

DAT_ADDITION='https://api.sheety.co/5216442781027898295e35fd5e724163/myWorkouts/workouts'
date = datetime.date.today().strftime('%d/%m/%Y')
time = datetime.datetime.now().strftime('%H:%M:%S')

EXERCISE_ENDPOINT='https://trackapi.nutritionix.com/v2/natural/exercise'
header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEYS
}

params = {
 "query":input("Enter The Exercise"),
 "gender":"male",
 "weight_kg":WEIGHT,
 "height_cm":HEIGHT,
 "age":AGE
}

data = requests.post(url=EXERCISE_ENDPOINT,json = params,headers=header)
print(data.json())
new_data1 = data.json()['exercises']

for i in new_data1:
    new_data = i
    info = {
        'workout':{'date':date,
                    'time':time,
                    'exercise':new_data['name'].title(),
                    'duration':new_data['duration_min'],
                    'calories':new_data['nf_calories']}
    }
    authorization={
        'Authorization':'Basic dmFjb20xMzoxMjM0NTY='
    }
    a = requests.post(url=DAT_ADDITION,json=info, headers = authorization)
    print(a.status_code)


