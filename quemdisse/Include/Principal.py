from textblob import TextBlob as tb
import tweepy
import json

api_key = 'iqrCqQr8J7f332I9DuQcEWMOw'
api_secret_key = 'FXIs5nadC9EzEuNLcC4wllBtcNsyXO88qVXvav84SKE2NfWa4l'
access_token = '1083387489644175363-AZtqmheHRvQ8r0OzQp9YLDNq6GkcnK'
access_token_secret = 'NQy73E2XDbCLnB7qqi5qOxfVydoTRJQ2MjeVuatmJlIm0'

autorizar = tweepy.OAuthHandler(api_key, api_secret_key)
autorizar.set_access_token(access_token, access_token_secret)
api = tweepy.API(autorizar)

file = open("testandoDados.json", "w", encoding='utf-8')
dado = []
dados = api.search('lula')
print(type(dados))

for tweet in dados:
    print(tweet.text)
    analisar = tb(tweet.text)
    polaridade = analisar.polarity
    print(polaridade)
    file.write(tweet.text)
    #dado.append(tweet.text)

#json.dump(dado, file)
file.close()
