import requests
import webbrowser
import sys
import datetime

links = []
keep = []

if (len(sys.argv) == 2):

	while not sys.argv[1].lower() == 'settings':

		sys.argv[1] = input("Please enter a correct argument\n")

	animal = ""

	while not (animal == "Dogs" or animal == "Cats" or animal == "Birds"):

		animal = input("DOGS or CATS or BIRDS?\n").lower()

		if animal == 'dogs' or animal == 'dog':

			animal = "Dogs" 

			extension = "shibes"

		elif animal == "cats" or animal == "cat":

			animal = "Cats"

			extension = "cats"

		elif animal == "bird" or animal == "birds":

			animal = "Birds"

			extension = "birds"

	num = -1

	while not num > 0 and num < 100:

		num = int(input("How many " + animal + " do you want to see?\n"))

else:

	animal = "Dogs"

	num = 10

	extension = "shibes"

url = "http://shibe.online/api/" + extension;

params = {'count': num, 'urls': 'true', 'httpsUrls': 'true'}

r = requests.get(url, params=params)

print(animal + " incoming!")

for dog in r.json():
	links.append(dog)
	webbrowser.open(dog, new=2)


cont = True;

while cont == True:

	try:
		add = int(input("Did you like any pictures you want to keep? Type in the number with 1 being the newest tab (Type 'stop' to finish)\n"))

		if add >= 1 and add <= num:

			index = num - add - 1

			keep.append(index)
			keep.append(links[index]) 

	except Exception as e:
		cont = False;

now = datetime.datetime.now()

time = now.strftime("%Y-%m-%d %H:%M")

fliename = animal + "links " + time + ".txt"

file = open(fliename, 'w');

for i in range(0, len(keep), 2):

	number = keep[i]
	link = keep[i + 1]

	file.write(str(number) + ") " + link + "\n")

file.close()




