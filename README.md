# SHOW-ME-SHIBE
a python script which shows you shibe 

## Description
Show Me Shibe is a simple python script which when run allows opens up to 100 pictures of either Shibe, Cats or Birds. You
can specifiy which animal you want to see and how many pictures you want to see. After viewing the pictures you are asked 
which photos you liked and those links are stored in a txt file for you to view later!

### Instructions
To run it, you must either clone or repository or just download the python script titled shibe.py. You will have to install
the requests python module as the script makes GET requests to the Shibe.Online Api. You can use pip to install the module. 

```pip install requests```

After installing requests, you can just run the python script and let the magic happen. 

```python3 shibe.py

To run the file and choose if you want Shibe, Cats or Dogs and how many pictures you want, just run the script with the
argument "settings".

```python3 shibe.py settings````

After viewing the photos, each photos is given a number and you can enter the number of the photos you liked and the
corresponding links will be opened in txt file. 

### Purpose
The purpose of this script was just so I could play around with GET requests and APIs. The Shibe.Online API stood out to 
me because it was just so cool. But other than the that, this was all just a little bit of fun.

### Future GOALS
Even though this project was pretty much a joke, that doesn't mean the grind stops here. My future goals are:
- [] Make the processing of adding links to the list more human proof (no repeats and in order)
- [] Email pictures to people
- [] Make this into an Alexa App

