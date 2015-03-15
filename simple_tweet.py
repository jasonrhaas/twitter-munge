#!/usr/bin/env python

import json
import sys
import pandas as pd
import numpy as np
import pylab
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

with open('/Users/jhaas/tweets.json', 'r') as thefile:
    tweets = [json.loads(line) for line in thefile]

x = range(1,len([tweet['created_at'] for tweet in tweets]))
y = [tweet['retweet_count'] for tweet in tweets]

# print x
s = pd.Series(y)

df = pd.DataFrame()
df['text'] = map(lambda tweet: tweet['text'], tweets)
df['lang'] = map(lambda tweet: tweet['lang'], tweets)
df['country'] = map(lambda tweet: tweet['place']['country']
if tweet['place'] != None else None, tweets)
df['retweet_count'] = [tweet['retweet_count'] for tweet in tweets]
# df['withheld_in_countries'] = [tweet['withheld_in_countries'] for tweet in tweets] if != None else None
# df['withheld_in_countries'] = []
# for tweet in tweets:
#     if tweet['withheld_in_countires']:
#         df['withheld_in_countries'].append(tweet['withheld_in_countires'])
#     else:
#         df['withheld_in_countries'].append('None')

df['screen_name'] = [tweet['user']['screen_name'] for tweet in tweets]
df['tweet_id'] = [tweet['id_str'] for tweet in tweets]
# try:
#     df['coordinates'] = [tweet['coordinates']['coordinates'] for tweet in tweets]
# except:
#     pass
df['created_at'] = [tweet['created_at'] for tweet in tweets]
# df['hashtags'] = [tweet['entities']['hashtags'] for tweet in tweets]
# df['urls'] = [tweet['entities']['urls'] for tweet in tweets]
# df['user_mentions'] = [tweet['entities']['user_mentions'] for tweet in tweets]


tweets_by_lang = df['lang'].value_counts()

#
# fig, ax = plt.subplots()
# ax.tick_params(axis='x', labelsize=15)
# ax.tick_params(axis='y', labelsize=10)
# ax.set_xlabel('Languages', fontsize=15)
# ax.set_ylabel('Number of tweets' , fontsize=15)
# ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
# tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

# pylab.show()
# df['text'] = [tweet['text'] for tweet in tweets]
#
# prepare some data
# x = tweets_by_lang.keys()
# y = tweets_by_lang.values
#
# # output to static HTML file
# output_file("lines.html", title="line plot example")
#
# # Plot a `line` renderer setting the color, line thickness, title, and legend value.
# p = figure(title="tweets by language")
# p.line(x, y, legend="Temp.", x_axis_label='x', y_axis_label='y')
#
# show(p)
