import tweepy
import ast
print "Welcome to Crosscut!"
print "please register an app at twitter. This will be streamlined in the future"
print "please set the app permission to 'read and modify direct messages'"

consumer_key = input("please paste your consumer key here ")
consumer_secret = input("please paste your consumer secret here ")
access_token = input("please paste your access token here ")
access_token_secret = input("please paste your access token secret here ")
user_id = input("please type your twitter user id ")



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
delete_list = []
search_messages = []
search_sender = []
#do_search_text = input('would you like to delete messages by searching message text? type "yes" or "no"')
#if do_search_text == 'yes':

delete_all = input("would you like to delete all DMs? type 'yes' or 'no'")
if delete_all == 'yes':
    messages = tweepy.Cursor(api.direct_messages, id=user_id).items()

    for message in messages:
        msg_id = str(message).split('sender_id=')[1].split('entities={')[0].split('id=')[1].strip(', ')
        api.destroy_private_message(id=msg_id)

else:
    while True
    message_text = input("please input the terms or phrases you'd like to delete. When are you finished, type  'done'")
    if message_text == 'done':
        break
    else:
        search_messages.append(message_text)
    print search_messages

    while True:
        sender_text = input("please input the senders you wish to delete messages from, when you are finished, type 'done'")
        if sender_text == 'done':
            break
        else:
            search_sender.append(sender_text)

#print search_sender
#print "this is search sender"
        #else:
#    pass

messages = tweepy.Cursor(api.direct_messages, id=user_id).items()

for message in messages:
    if delete_all == 'yes':
        msg_id = str(message).split('sender_id=')[1].split('entities={')[0].split('id=')[1].strip(', ')
        api.destroy_private_message(id=msg_id)
    else:
        for search in search_messages:
            message_text = str(message).split('text=u')[1].split(' ,')
            print message_text
            if search in message_text:
                delete_tweet = input('would you like to delete '+ message_text+'? type "yes" or "no" ')
            if delete_tweet == "yes" or "y" or "okay":
                msg_id = str(message).split('sender_id=')[1].split('entities={')[0].split('id=')[1].strip(', ')
                api.destroy_direct_message(id=msg_id)






        for sender in search_sender:
            sender_name = ast.literal_eval(str(message).split(' _json=')[1].split(', time_zone')[0])['screen_name']
            if sender_name == sender:
            #message_text = str(message).split('text=u')[1].split(', created_at')[0]
            #delete_ok = input("would you like to delete message " + message_text + " from " + sender)
                msg_id = str(message).split('sender_id=')[1].split('entities={')[0].split('id=')[1].strip(', ')
                delete_list.append(msg_id)
            else:
                continue
        #print delete_list
            delete_ok = input('would you like to delete all messages from ' + sender + '? type "yes" or "no"')

            if delete_ok == "yes" or "y" or "ok":
                for message in delete_list:
                    try:
                        api.destroy_direct_message(id=msg_id)
                    except:
                        print "shit something went wrong"
                    pass
            else:
                print("messages from " + sender + " were not deleted")
