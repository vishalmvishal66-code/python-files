from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday:', birthday_date)


# sometimes you receive the date as string and need to 
# a datetime object this without exception handling function 