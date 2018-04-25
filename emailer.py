import requests

def get_emails():
  emails = {}

  try:
    email_file = open('emailsdoc.txt', 'r')

    for line in email_file:
      (email, username) = line.split(',')
      emails[email] = username.strip()
  except FileNotFoundError as err:
    print(err)  

  return emails 

def get_schedule():
  try:
    schedule_file = open('schedule.txt', 'r')
    schedule = schedule_file.read()
  except FileNotFoundError as err:
    print(err)

  return schedule

def get_weather_forecast():
  url = 'http://api.openweathermap.org/data/2.5/weather?q=Allen&units=imperial&appid=6b78bf20d0d8dc61a03d179758d9f959' 
  weather_request = requests.get(url)
  weather_json = weather_request.json()
  print(weather_json)

def main():
  emails = get_emails()
  schedule = get_schedule()
  get_weather_forecast()

  print(emails)
  print(schedule)

main()

