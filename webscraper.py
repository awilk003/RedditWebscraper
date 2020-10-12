# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:55:25 2020

@author: Alex
"""


import praw
import pandas as pd

reddit = praw.Reddit(client_id='k3z1Q3Is8QXf9w', 
                     client_secret='ZN7GL5mBSoW06L5HozwJRrEvvOQ',
                     user_agent='Reddit WebScrape')


posts = []
PH_subreddit = reddit.subreddit('ProgrammingHumor')

for post in PH_subreddit.top(limit=10):
    posts.append([post.title, post.author, post.score, post.id, post.subreddit,
                  post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title','author', 'score', 'id',
                                    'subreddit', 'url', 'num_comments',
                                    'body', 'created'])
print(posts)


posts.to_csv (r'C:\Users\Alex\Desktop\CS\webscrape\export_dataframe.csv',
              index = False, header=True)