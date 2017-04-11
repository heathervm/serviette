#delete your tweets!
import tweepy
import ast
print "Welcome to Serviette!"
print "please register an app at twitter. This will be streamlined in the future"
print "please set the app permission to 'read and modify tweets'"

consumer_key = input("please paste your consumer key here ")
consumer_secret = input("please paste your consumer secret here ")
access_token = input("please paste your access token here ")
access_token_secret = input("please paste your access token secret here ")
user_id = input("please type your twitter user id ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweet_sheet = []
retweet_sheet = []
delete_sheet = []
terms_to_delete = []

while True:
    search_term = (input("please input the terms or phrases you'd like to delete, in quotes. When you are done entering terms, type 'done' "))
    if search_term != 'done':
        terms_to_delete.append(search_term)
    if search_term == 'done':
        break
print "you are searching for:"
print terms_to_delete

for status in tweepy.Cursor(api.user_timeline, id=user_id).items():
    try:
        tweet_sheet.append(ast.literal_eval(str(status).split(' _json=')[2].split(', coordinates')[0]))
    except:
        try:

            retweet_sheet.append(ast.literal_eval(str(status).split(' _json=')[1].split(', coordinates=None')[0]))

        except:
            print "something went wrong"
            pass


for i in range(len(tweet_sheet)):
    for term in terms_to_delete:
        if term in tweet_sheet[i]['text']:
            try:
                delete_sheet.append(tweet_sheet[i])
            except:


                pass
        else:
            pass




for i in range(len(retweet_sheet)):
    for term in terms_to_delete:
        if term in retweet_sheet[i]['quoted_status']['text'] or retweet_sheet[i]['text']:
            try:
                delete_sheet.append(retweet_sheet[i])
            except:

                pass
            else:
                pass

for i in range(len(delete_sheet)):
    if len(delete_sheet) > 0:
        try:
            ans = input("would you like to delete " + str(delete_sheet[i]['text']))
        except:
            print delete_sheet[i]
            pass

        if ans == "yes" or "y" or "ok" or "sure":
            api.destroy_status(delete_sheet[i]['id'])
        else:
            print "ok this tweet will be saved"
    else:
        print("there are no tweets to delete")
