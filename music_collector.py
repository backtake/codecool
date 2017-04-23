import csv
import datetime
import random
import sys

def music_csv():

    music = []
    with open("music.csv", "r") as infile:
        reader = csv.reader(infile)
        for row in reader:
            item0 = (row[0], row[1])
            item1 = (int(row[2]), row[3], row[4])
            music.append((item0, item1))
        return music


def adding_collection():
    while True:     #adding name of the artist
        artist = input("Add name of the artist: \n")
        if artist == '':
            print("You must enter name of the artist!")
        else:
            break

    while True:     #adding name of the album
        album = input("Add name of the album: \n")
        if album == '':
            print("You must enter name of the album!")
        else:
            break

    while True:     #adding year of the album
        year=input("Enter year of the adding album: \n")
        try:
            year=int(year)
        except ValueError:
            print("Year has to be Integer!!")
            continue
        if (year < 1000 or year > 9999):
            print("Year has to be written with four digits!")
            continue
        elif (year >= 1000 and year <=9999):
            break

    while True:     #adding genre of the adding album
        genre = input("Add genre of the album: \n")
        if album == '':
            print("You must enter genre of the album!")
        else:
            break

    while True:     #adding lenght of the adding album
        minutes=input("How many minutes adding album is long? \n")
        seconds=input("And seconds? \n")
        try:
            minutes=int(minutes)
            seconds=int(seconds)
        except ValueError:
            print("Lenght of the album has to be Integer!!")
            continue
        if (minutes < 0 or seconds < 0 or seconds > 60):
            print("oh come on! You can't even add a proper data?!")
        else:
            lenght = ("{}:{}".format(minutes, seconds))
            break

    with open('music.csv', 'a') as infile:  #saving to the file
        adding = csv.writer(infile)
        adding.writerow([artist] + [album] + [year] + [genre] + [lenght])


def find_album_by_artist(): #you type ur artist ill type his album
    music=music_csv()
    artist_name=input("Which artist's album are you looking for? ").lower()
    a=0 #zmienna do liczenia ilosci wystapien dopasowan 
    for item in music:
        if item[0][0].lower()==artist_name:
            print(item[0][0],":",item[0][1])
            a+=1 #za kazdy znaleziony item dodajemy 1 do wartosci a
    if a == 0: #jesli nie ma dopasowan to:
        print("Our music collector is not big enough, sorry! :(")





def find_album_by_year():  #you type ur year ill type its album
    music=music_csv()
    while True:         #checking if u typed a year
        year = input("From which year is album you are looking for? ")
        try:
            year = int(year)
            break
        except ValueError:
            continue
    a=0 #zmienna do liczenia ilosci wystapien dopasowan     
    for item in music:
        if item[1][0]==year:
            print(item[0][0],":",item[0][1])
            a+=1 #za kazdy znaleziony item dodajemy 1 do wartosci a
    if a == 0: #jesli nie ma dopasowan to:
        print("Our music collector is not big enough, sorry! :(")        


def find_artist_by_album(): #finding for you artist by typed album
    music=music_csv()
    album=input("Which album's author are you looking for? ").lower()
    a=0 #zmienna do liczenia ilosci wystapien dopasowan
    for item in music:
        if len(album)>1 and album in item[0][1].lower():
            print(item[0][0],":",item[0][1])
            a+=1 #za kazdy znaleziony item dodajemy 1 do wartosci a
    if a == 0: #jesli nie ma dopasowan to:
        print("Our music collector is not big enough, sorry! :( I can't find what you're looking for..")        

def find_album_by_letters(): #finding for you album by typed letter(s)
    music=music_csv()
    letters=input("Type just the part of the album you are looking for: ").lower()
    a=0 #zmienna do liczenia ilosci wystapien dopasowan
    for item in music:
        if letters in item[0][1].lower():
            print(item[0][0],":",item[0][1])
            a+=1 #za kazdy znaleziony item dodajemy 1 do wartosci a

    if a == 0: #jesli nie ma dopasowan to:
        print("Our music collector is not big enough, sorry! :( I can't find what you're looking for..")


def find_album_by_genre():  #finding for you album by typed genre
    music=music_csv()
    genre=input("What kind of music are you looking for? ").lower()
    a=0 #zmienna do liczenia ilosci wystapien dopasowan
    for item in music:
        if genre in item[1][1].lower():
            print(item[0][0],":",item[0][1])
            a+=1 #za kazdy znaleziony item dodajemy 1 do wartosci a

    if a == 0: #jesli nie ma dopasowan to:
        print("Our music collector is not big enough, sorry! :( I can't find what you're looking for..")


def total_age_of_all_albums():  #doing serious math, adding up age of all your albums
    music=music_csv()
    now = datetime.datetime.now()
    total_age=0
    for item in music:
        total_age+=now.year - item[1][0]
    print("Total age of all albums is: ",total_age)


def random_album_by_genre():    #picking a random album by genre
    music=music_csv()
    lottery_of_genres=[]
    genre=input("What kind of music are you looking for? ").lower()
    a=0 #zmienna do liczenia ilosci wystapien dopasowan
    for item in music:
        if genre in item[1][1].lower():
            lottery_of_genres.append(item)
            a+=1 #za kazdy znaleziony item dodajemy 1 do wartosci a
    if len(lottery_of_genres)>0:
        random_genre=random.choice(lottery_of_genres)
        print(random_genre[0][0],":",random_genre[0][1])
    if a == 0: #jesli nie ma dopasowan to:
        print("Our music collector is not big enough, sorry! :( I can't find what you're looking for..")

  

while True:
    print("*"*80)
    print("""\nWelcome in the CoolMusic!
         1) Add new album
         2) Find albums by artist
         3) Find albums by year
         4) Find musician by album
         5) Find albums by letter(s)
         6) Find albums by genre
         7) Calculate the age of all albums 
         8) Choose a random album by genre
         0) Exit""")
    print("")     
    print("*"*80)
    try:
        action = int(input("\nChoose option from the menu: "))
    except ValueError:
        continue
    if action == 1:
        adding_collection()
    elif action == 2:
        find_album_by_artist()
    elif action == 3:
        find_album_by_year()
    elif action == 4:
        find_artist_by_album()
    elif action == 5:
        find_album_by_letters()
    elif action == 6:
        find_album_by_genre()
    elif action == 7:
        total_age_of_all_albums()
    elif action == 8:
        random_album_by_genre()
    elif action == 0:
        sys.exit()
    else:
        print("There is no such option")





