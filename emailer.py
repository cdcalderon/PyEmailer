emails = {}

try:
  email_file = open('emailsdoc.txt', 'r')

  for line in email_file:
    (email, username) = line.split(',')
    emails[email] = username.strip()
except FileNotFoundError as err:
  print(err)  

print(emails)

try:
  schedule_file = open('schedule.txt', 'r')
  schedule = schedule_file.read()

  print(schedule)
except FileNotFoundError as err:
  print(err)

