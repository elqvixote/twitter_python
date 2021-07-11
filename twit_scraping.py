# Bot de twitter
# la dependencia json es para visualizar mejor la información

import tweepy
import json

# 4 cadenas de autenticación
consumer_key = "ingresar código acá"
consumer_secret = "ingresar código acá"
access_token = "ingresar código acá"
access_token_secret = "ingresar código acá"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#wait es para que en caso de llegar al limite el programa no se caiga sino que espere 
api = tweepy.API(auth, wait_on_rate_limit=(True), wait_on_rate_limit_notify=(True))

# Obtener información de mi propia cuenta
data = api.me()
print(json.dumps(data._json, indent=2))

# Obtener información de otra cuenta
data = api.get_user("nike")
print(json.dumps(data._json, indent=2))

#Obtener followers de un ususario
datafoll = api.followers(screen_name="nike")

# la api nos da la información paginada de a 20 como se ve a continuación:
#print(len(datafoll))
#for user in datafoll:
#    print(json.dumps(user._json, indent = 2))

# Para no limitarnos por la paginación
# .items es la cantidad de datos que queremos
# hay que iterar con la variable que queremos
for user in tweepy.Cursor(api.followers, screen_name = "nike").items(50):
    print(json.dumps(user._json, indent=2))
    
# friends son las persons que sigue la cuenta
# followers son las personas que siguen a la cuenta

for user in tweepy.Cursor(api.friends, screen_name = "nike").items(50):
    print(json.dumps(user._json, indent=2))    
    
#Obtener un Timeline
# tweet_mode es para definir el tamaño del tuit
# .items es la cantidad de datos que queremos
for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike", tweet_mode="extended").items(1):
    print(json.dumps(tweet._json, indent=2))

#Buscar tweets
# q es para búsqueda de texto
for tweet in tweepy.Cursor(api.search, q = "lucha de clases", tweet_mode="extended").items(10):
#    print(json.dumps(tweet._json, indent=2))
# para extraer solo el texto 
    print(tweet._json["full_text"])
