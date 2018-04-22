emails = []
email_file = open('emailsdoc.txt', 'r')

for line in email_file:
  emails.append(line)

print(emails)