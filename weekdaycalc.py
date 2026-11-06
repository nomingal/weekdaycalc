import os
import math

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def askform():
    clear()
    return int(input("Enter date format:\n\n1- MM/dd/yyyy\n2- dd/MM/yyyy\n3- yyyy/MM/dd\n\n"))

dateform = askform()

while dateform > 3 or dateform < 1:
    dateform = askform()

clear()

def askdate():
    return input("Enter a date between 1753 and 2099: ")

date = askdate()

while not len(date) == 10:
    clear()
    print(f'Wrong format, follow {"MM/dd/yyyy" if dateform == 1 else "dd/MM/yyyy" if dateform == 2 else "yyyy/MM/dd"} format')
    date = askdate()

if dateform == 1 or dateform == 2:
    while date[2] != "/" or date[5] != "/":
        clear()
        print(f'Wrong format, follow {"MM/dd/yyyy" if dateform == 1 else "dd/MM/yyyy"} format')
        date = askdate()
else:
    while date[4] != "/" or date[7] != "/":
        clear()
        print("Wrong format, follow yyyy/MM/dd format")
        date = askdate()

if dateform == 1:
	d = int(date[3:5])
	m = int(date[0:2])
	y = int(date[8:10])
	s = int(date[6:8])

elif dateform == 2:
	d = int(date[0:2])
	m = int(date[3:5])
	y = int(date[8:10])
	s = int(date[6:8])

else:
	d = int(date[8:10])
	m = int(date[5:7])
	y = int(date[2:4])
	s = int(date[0:2])

mcode = {
	1: 1,
	2: 4,
	3: 4,
	4: 0,
	5: 2,
	6: 5,
	7: 0,
	8: 3,
	9: 6,
	10: 1,
	11: 4,
	12: 6
}

seccode = {
	17: 4,
	18: 2,
	19: 0,
	20: -1
}

day = {
	0: "Saturday",
	1: "Sunday",
	2: "Monday",
	3: "Tuesday",
	4: "Wednesday",
	5: "Thursday",
	6: "Friday"
}

year = str(s) + str(y)
year = int(year)
y = int(y)
schan = seccode[s]
mchan = mcode[m]

if year % 4 == 0 and m == 1:
	mchan = 0
elif year % 4 == 0 and m == 2:
	mchan == 3

rest = (y + math.floor(y / 4) + schan + d + mchan) % 7
result = day[rest]
clear()
print(f"{date} is a {result}")