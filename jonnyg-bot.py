import praw
import config 
import time
import os
import random

trigger_word = ['Jonny', 'Jonathan', "Jon"]
comment_reply = [
                'Im not a vegetable', 'I will not control myself', 'idk but Thom is getting facefucked', 
                'I love when Thom doesnt wash for a few days', '*tries to play idioteque faster*', 'we are a testosterone free band',
                'I love Penderecki', '/uj Thom is my wife', 'Thom feet', '*touches Thom under his pants*', "Im saggitarius",
                "Im pampered like you wouldnt believe", 'Makes me wanna go cottaging', "I hear that A LOT", "Slower Thom",
                "Sex", "Thom said I was supposed to play faster, and I did play faster, but it wasnt enough! IT WASNT ENOUGH FOR THOM!!!",
                'Israel'
                ]

thom_reply = ['Hi, my beloved tomcat', '', "Thom Thom, wanna go cottaging?", 'Slower Thom', 'I told you im not a vegetable :(', 'Touches Thom where sun doesnnt shine']

def bot_login():
    print("logging in...")
    r= praw.Reddit(username = config.username, 
           password = config.password,
           client_id = config.client_id,
           client_secret = config.client_secret,
           user_agent = config.user_agent)
    print("logged in")
    return r

def run_bot(r, comments_replied_to):
    # D  E B U G print ("obtaining comments")

    for comment in r.subreddit('radioheadcirclejerk').comments(limit=25):
        if "jonny" in comment.body and comment.id not in get_saved_comments() and comment.author != r.user.me():

            print ("string found in comment " + comment.id)

            comment.reply(random.choice(comment_reply))

            print("replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open('comments_replied_to.txt', 'a') as f:
                f.write(comment.id + '\n')

        if "Jonny" in comment.body and comment.id not in get_saved_comments() and comment.author != r.user.me():

            print ("string found in comment " + comment.id)

            comment.reply(random.choice(comment_reply))

            print("replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open('comments_replied_to.txt', 'a') as f:
                f.write(comment.id + '\n')

        if "Jon" in comment.body and comment.id not in get_saved_comments() and comment.author != r.user.me():

            print ("string found in comment " + comment.id)

            comment.reply(random.choice(comment_reply))

            print("replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open('comments_replied_to.txt', 'a') as f:
                f.write(comment.id + '\n')

        if "jon" in comment.body and comment.id not in get_saved_comments() and comment.author != r.user.me():

            print ("string found in comment " + comment.id)

            comment.reply(random.choice(comment_reply))

            print("replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open('comments_replied_to.txt', 'a') as f:
                f.write(comment.id + '\n')

        if "Jonathan" in comment.body and comment.id not in get_saved_comments() and comment.author != r.user.me():

            print ("string found in comment " + comment.id)

            comment.reply(random.choice(comment_reply))

            print("replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open('comments_replied_to.txt', 'a') as f:
                f.write(comment.id + '\n')

        #if comment.author == r.user() and comment.author != r.user.me():
            #print('Thombot detected')
            #comment.reply(random.choice(thom_reply))

    # D E B U G print('sleep')
    time.sleep(60) 
      

def get_saved_comments():
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []

    else:
        with open('comments_replied_to.txt', 'r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split('\n')
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to

r = bot_login()

comments_replied_to = get_saved_comments()
print (comments_replied_to)

while True:
    run_bot(r, comments_replied_to)