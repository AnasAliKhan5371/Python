# A personalised greeting program in Python demonstrates the use of variables and data types to create dynamic and interactive output.
import datetime

name=input("Enter Name : ")

now=datetime.datetime.now()
hour=now.hour

if 5<= hour< 12:
    greeting="Good Morning"
elif 12<= hour< 18:
    greeting="Good Afternoon"
else:
    greeting="Good Night"

personal=f"{greeting},{name}! Welcome to Python."

print(personal)