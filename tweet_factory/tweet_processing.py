#Tweepy wrapper imports
import tweepy
from tweepy.auth import OAuthHandler

#Twitter API authentication fields
CONSUMER_KEY = "Bk2RrrGJIx3z3R3NzWXk2V0g0"
CONSUMER_SECRET = "Q5QPiTiapz1GewGV2aeLWoT8IoWXhjBFrC9bsQRvjOjpTSacPK"
TOKEN_KEY = "435217839-v08vYEBqddJQYHmH42ih269a6QsY0G4SozqEbs4P"
TOKEN_SECRET = "aYREePRSAlWpPyBQvs3VOYbHnt8w2UZCWyTj21yGzQGzW"

#This handles Twitter authetification and the connection to Twitter Streaming API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

#Squad list
squads = ["ManUtd","SwansOfficial","BurnleyOfficial","WBAFCofficial","whufc_official","LCFC","SpursOfficial","HullCity","CPFC","QPRFC","SouthamptonFC","stokecity","NUFC","Arsenal","SunderlandAFC","AVFCOfficial","ChelseaFC","LFC","Everton","MCFC"]

#Hash to store squads tweet information: tweet id,
screen_names = {}

#Number of tweets to consider
n_tweets = 1000

#Procedure to initialize hash values
def init_hash():
    for squad in squads:
        screen_names[squad] = {}

#Procedure to update hash values
def update_hash(screen_name):
    since_id = "662035721235136512"
    max_id = "663589373770932224"
    search_results = api.search(q=screen_name,since_id="662035721235136512",max_id="663589373770932224")
    for search_result in search_results:
        screen_names[screen_name][search_result.id_str] = ""

#Main procedure called by Flask app
def tweet_processing():
    #Initialize hash
    init_hash()
    #Update hash
    for screen_name in screen_names.keys():
        update_hash(screen_name)
    return screen_names
