import time

birth_year = int(input('What year were you born' + "\n"))
today_year = time.localtime().tm_year

print('You are {} years old. Sorry about that! :)'.format(today_year - birth_year))