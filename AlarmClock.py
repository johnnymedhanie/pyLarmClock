import os
import time
import webbrowser
import sys
import builtins
import random

if os.path.isfile("collection.txt") == False:
    print
    'FATAL: collections doesn\'t '
    print
    "Creating a file now.."
    op = os.O_CREAT | os.O_WRONLY
    create = os.open("collection.txt", op)
    with os.fdopen(create, 'w') as newCollection:
        newCollection.write("https://www.youtube.com/watch?v=GibiNy4d4gc")

print("When do you want to start your alarm?")
print("Input as 00:00")
alarmTime = input("time?")

with open("collection.txt") as collection:
    videos = collection.readline()


currentTime = time.strftime("%H:%M")

while currentTime != alarmTime:
    print('it is currently' + currentTime + 'and your alarm is set for' + alarmTime)
    currentTime = time.strftime("%H:%M")
    time.sleep(5)

if currentTime == alarmTime:
    print("Wake up")
    linkvideo = random.choice(videos)
    webbrowser.open(linkvideo)




