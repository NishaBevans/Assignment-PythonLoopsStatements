#1: The Range Riddle:
#Task 1: Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic",
#and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it. 
#Ensure that your program includes the use of the random module to select the mood.
#Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."

import random
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
mood_list = ["happy", "sad", "calm", "stressed", "excited", "frustrated", "confident"]


i = 0

for day in range(7):
    mood = random.choice(mood_list)
    print(days[i], "I was feeling " + mood)
    i = i + 1
