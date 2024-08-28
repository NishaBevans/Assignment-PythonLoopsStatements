#Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening)
#for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should 
#iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again 
#to randomly select the mood.

import random
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]
mood_list = ["happy", "sad", "calm", "stressed", "excited", "frustrated", "confident"]

i = 0

for day in range(7):
    mood = random.choice(mood_list)
    time = random.choice(time_of_day)
    print("On", days[i], time, "I was feeling " + mood)
    i = i + 1


