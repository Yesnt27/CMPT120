# Assignment 3: Billboard Top 100
# Kenny Nguyen
# October 19th, 2024

import pathlib

# Open the data file
#Wave have to tell Python where to find the file, and the file's name.
#   a) Get name of folder where this code is saved
folder_of_code = pathlib.Path(__file__).parent.resolve()

hot_100 = f"{folder_of_code}/hot-100-May2024.csv"
#   c) Open the file
my_file = open(hot_100)

user_name = input("What is your name? ")
if not user_name:
    print("You have no name.")
else:
    print("Greetings, "+user_name)
#skip over header line
unused_header_line=my_file.readline()
#list of variables for part 1:
#number of songs including 'love'
#song names that are in top 1 and 2
#artists whose name starts in 'A' (case sensitive)
print("Welcome to the Billboard top 100 app!")
print()
print("*"*25)
print("PART 1: Statistics & Data")
print("*"*25)
love_songs = 0
top_songs = []
A_name_list = []
top_artists_amt = 0
A_name_artists = 0
avg_weeks = 0
num_of_avg_songs = 0
advancing_songs = 0

for songs in my_file:
    clean_line = songs.strip()
    split = clean_line.split(",")
    if "love".strip("?!, $") in split[2].lower():
        love_songs += 1
    if(int(split[4]) == 1 or int(split[4]) == 2):
        top_songs.append(split[2])
        top_artists_amt +=1
    if(split[3].startswith('A')):
        A_name_artists+=1
        A_name_list.append(split[3])
    if(split[-1]):
        avg_weeks += int(split[-1])
        num_of_avg_songs+=1
    if (split[4]).isdigit():
        if(int(split[4]) > int(split[1])):
            advancing_songs +=1     
        elif int(split[4]) == 0:
            advancing_songs +=1
   
print(f"Number songs containing the word 'love': {love_songs}")
print()
print(f"Song names in rank positions 1 or 2: {top_artists_amt}")
for i in top_songs:
    print("- "+i)
print()
print(f"Artist names starting with 'A': {A_name_artists}")
for i in A_name_list:
    print("- "+i)
print()
print(f"Songs advancing in rank wrt previous week: {advancing_songs}")
print(f"Average weeks on board all songs: {float(avg_weeks / num_of_avg_songs):.3}")   
print()
#PART 2: User interaction
print("*"*24)
print("PART 2: User Interaction")
print("*"*24)

my_file.seek(0)
print()
first_query = input("First query: Artist name (may be part of the name): ").lower().strip()
check1 = False
if first_query != "":

    print(f"{'ARTIST':<50} {'SONG':<45} {'DATE':<15} {'RANK':>8} {'PREVIOUS RANK':>15}")
    for songs in my_file:
        clean_line = songs.strip()
        split = clean_line.split(",")
        if first_query.strip("?!, $") in split[3].lower():
            check1 = True
            print(f"{split[3]:<50} {split[2]:<45} {split[0]:<15} {split[1]:>8} {split[4]:>15}")
    if check1 == False:
        print("There is no such artist in the file.")
        
else:
    print("There is no such artist in the file.")
    

my_file.seek(0)
print()
second_query = input("Second query: Song title (may be part of the name): ").lower().strip()
weeks_on_board = 0
check = False
if second_query != "":
    for songs in my_file:
        clean_line = songs.strip()
        split = clean_line.split(",")
        if second_query.strip("?!, $") in split[2].lower():
            print(f"{'REQUESTED_SONG':<35} {'DATE':<23} {'WEEKS ON BOARD':<10}")
            print(f"{split[2]:<35} {split[0]:<35} {split[-1]:<35}")
            weeks_on_board += (int(split[-1]))
            check = True
            break
        else:
            check == False


    if check == True:
        print()
        print("Songs with more weeks on board than the requested song:")
        print()
        print(f"{'SONG':<35} {'DATE':<20} {'EXTRA WEEKS ON BOARD':<35}")
    my_file.seek(0)
    unused_header_line2=my_file.readline()
    if check == True:
        for songs in my_file:
            clean_line = songs.strip("?.,! ")
            split = clean_line.split(",")
            current_week = split[-1]
            if(weeks_on_board < int(current_week)):
                print(f"{split[2]:<35} {split[0]:<35} {(int(split[-1])-weeks_on_board):>5}")
    else:
        print("No songs matched that name")
    print()
else:
    print("No songs matched that name")
    print()
