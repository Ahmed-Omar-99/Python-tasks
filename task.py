# def add_commas_and_underscore(number):

#     number = f'{number:,}'

#     # Check that there is at least one symbol from the right
#     if(number[-4:-3] == ','):

#         # Get first symbol from the right
#         number = number[:-4] + '_' + number[-3:]

#     return number


# print(add_commas_and_underscore(12))
# print(add_commas_and_underscore(123))
# print(add_commas_and_underscore(1234))
# print(add_commas_and_underscore(123412345623476))
# print(add_commas_and_underscore(12344553423423462346))


# def Smart_Comment(title):

#     title = f'===== {title} ====='

#     print('=' * len(title))
#     print(title)
#     print('=' * len(title))

# Smart_Comment('Books')
# Smart_Comment('Web')
# Smart_Comment('Elzero')
# Smart_Comment('Elzero Web School')
# Smart_Comment('Ahmed Omar')

# import datetime

# print(datetime.datetime.now())

# print(dir(datetime.datetime.time()))

# y = datetime.datetime.now().year
# m = datetime.datetime.now().month
# d = datetime.datetime.now().day
# h = datetime.datetime.now().time().hour
# min = datetime.datetime.now().time().minute
# s = datetime.datetime.now().time().second

# s = s + 60
# min = min + 60
# h = h + 100
# d = d + 20

# if (s > 60):
#     min = min + (int(s / 60))
#     s = s % 60

# if (min > 60):
#     h = h + (int(min / 60))
#     min = min % 60

# if (h > 24):
#     d = d + (int(h / 24))
#     h = h % 24

# if (d > 24):
#     d = d + (int(h / 24))
#     h = h % 24


# print(d)
# print(h)
# print(m)
# print(s)

#import the time module
import time

current_time = time.time()

s = 50
m = 50
h = 23
d = 20

s = s + (m * 60)
s = s + (h * 60 * 60)
s = s + (d * 24 * 60 * 60)

endTime = s + current_time

# print(current_time)
# print(endTime)
