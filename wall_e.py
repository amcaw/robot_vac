
# -*- coding: utf-8 -*-

# vactrack.py code by @thetafferboy

import os
import pandas as pd
import tweepy
from datetime import datetime

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

# Pop Belgium
population_of_be = 9209116

bar_total = 15
perc_per_bar = 100/bar_total

from datetime import date, timedelta
date_to_check = (date.today() - timedelta(1)).isoformat()

data_read = pd.read_csv(
    'https://raw.githubusercontent.com/amcaw/robot_vac/main/result.csv', delimiter=',')

def AddDataToTweet(dataValue):
    dataToAdd = ''
    total_vacs = data_read.loc[data_read.DATE == date_to_check, dataValue].values[0]
    perc_rounded = round( ((total_vacs / population_of_be) * 100),2)
    solid_bars_to_print = perc_rounded // perc_per_bar
    empty_bars_to_print = bar_total - solid_bars_to_print

    dataToAdd
    while solid_bars_to_print > 0:
        dataToAdd += '▓'
        solid_bars_to_print -=1

    while empty_bars_to_print > 0:
        dataToAdd += '░'
        empty_bars_to_print -= 1

    dataToAdd += ' ' + str(perc_rounded) + '%\n\n'
    return dataToAdd


def SourceAndSendTweet(stringToTweet):
    stringToTweet += 'En date du '+str(date_to_check)+'\n'
    stringToTweet += 'Source : open data de Sciensano'
    print(stringToTweet)
    api.update_status(stringToTweet)

stringToTweet = ''
stringToTweet += 'Pourcentage de la population adulte ayant reçu le booster en Belgique \n\n'
stringToTweet += AddDataToTweet('E')
SourceAndSendTweet(stringToTweet)
