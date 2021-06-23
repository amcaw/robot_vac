
# -*- coding: utf-8 -*-

# vactrack.py code by @thetafferboy

import os
import pandas as pd
import tweepy
from datetime import datetime

# Twitter authorisation - you need to fill in your own API details (https://dev.twitter.com)
auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

# Pop Belgium
population_of_be = 9209116

# How many blocks you want in progress bar, 15 works well with Twitteer ▓▓▓▓▓░░░░░░░░░░
bar_total = 20
perc_per_bar = 100/bar_total

# This sets date to 2 days ago, as there is a lag in government data reporting. API requests will fail if you request date which has no data yet
from datetime import date, timedelta
date_to_check = (date.today() - timedelta(1)).isoformat()

# GOV UK data source API:
data_read = pd.read_csv(
    'https://app.workbenchdata.com/workflows/145128/steps/step--_mQtXYubHPE/current-result-table.csv', delimiter=',')

def AddDataToTweet(dataValue, textValue):
    dataToAdd = ''
    total_vacs = data_read.loc[data_read.DATE == date_to_check, dataValue].values[0]
    perc_rounded = round( ((total_vacs / population_of_be) * 100),2)
    solid_bars_to_print = perc_rounded // perc_per_bar
    empty_bars_to_print = bar_total - solid_bars_to_print

    dataToAdd += textValue
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
    stringToTweet += 'Source : open data de Sciensano\n'
    stringToTweet += 'Pop. de 18 ans et + au 01/01/2021\n'
    print(stringToTweet)
    api.update_status(stringToTweet)

stringToTweet = ''
stringToTweet += AddDataToTweet('CumuleA','% de Belges ayant reçu au moins une dose: \n\n')
stringToTweet += AddDataToTweet('CumuleB','% de Belges totalement vaccinés: \n\n')
SourceAndSendTweet(stringToTweet)
