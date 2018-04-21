# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 18:35:42 2018

@author: Chat
"""
import pip


def install(): # Run this to install the matplotlib dependency.
    pip.main(['install', 'matplotlib'])

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import praw
import datetime
# Fixing random state for reproducibility

def hour_to_count(y, hours_and_count):
    for x in y:
        hours_and_count[x] = (y.count(x))
        while x in y:
            y.remove(x)
    return y

reddit = praw.Reddit(client_id='ID',
                     client_secret='SECRET',
                     password='REDDIT_PASSWORD',
                     user_agent='USER_AGENT',
                     username='USERNAME')
submissions = []
keys = []
values = []
y = []
hours_and_count = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0}
SUBREDDIT = 'Python'
LIMIT = 1000

subreddit = reddit.subreddit(SUBREDDIT)
for submission in subreddit.new(limit=LIMIT):
    submissions.append(vars(submission)) #Converts Reddit Post Objects to Dicts. Makes it easier to analyze 

    
    


i = len(submissions) - 1
while i >= 0:
    y.append(int(datetime.datetime.fromtimestamp(int(submissions[i]['created_utc'])).strftime('%H')))
    i -= 1


hour_to_count(y, hours_and_count)
if len(y) > 0:
    hour_to_count(y, hours_and_count)
s = 100

for key in hours_and_count:
    keys.append(key)
for x in hours_and_count.values():
    values.append(x)
    
plt.scatter(keys, values, s, c="b", alpha=0.5)
plt.xlabel("Time")
plt.ylabel("Number of Posts")
plt.legend(loc=2)
plt.show()

if sum(values) == len(submissions):
    print("Data is valid")
    input("Press any key to exit")
else:
    print("Data does not add up to the limit. Check limit and subreddit")
    input("Press any key to exit")

