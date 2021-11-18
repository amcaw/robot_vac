import os
import pandas as pd
import tweepy
from datetime import datetime

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

df = pd.read_csv(
    'https://raw.githubusercontent.com/amcaw/robot_vac/main/result_hospi.csv', delimiter=',')
    
hospi1 = df.iloc[0,2]
hospi2 = df.iloc[0,3]

texte = (F"En Belgique, {hospi1} patients sont actuellement hospitalisés en lien avec le Covid-19, dont {hospi2} patients traités en soins intensifs")

print(texte)
api.update_status(texte)
