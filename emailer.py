emails = []

try:
  email_file = open('emailsdoc.txt', 'r')

  for line in email_file:
    emails.append(line.strip())
except FileNotFoundError as err:
  print(err)  

print(emails)