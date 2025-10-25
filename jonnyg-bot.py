import praw
import time
import os
import random
from comment_reply import comment_reply
from comment_reply import thombot_reply

def bot_login():
    print("logging in...")
    r= praw.Reddit('JonnyGreenwod-bot')
    print("logged in")
    return r

def run_bot(r, comments_replied_to):
    # D  E B U G print ("obtaining comments")
    trigger_word = ['Jonny', 'Jonathan', "Jon",'jon','jonny','jahnee','Greenwood','greenwod','greenwood']
    # tests = [trigger in comment.body for trigger in trigger_word]

    for comment in r.subreddit('radioheadcirclejerk').comments(limit=25):
        if any(trigger in comment.body for trigger in trigger_word) and comment.id not in get_saved_comments() and comment.author != r.user.me():

            print ("string found in comment " + comment.id)

            comment.reply(random.choice(comment_reply))

            print("replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open('comments_replied_to.txt', 'a') as f:
                f.write(comment.id + '\n')

        # if "Jonny" in comment.body and comment.id not in get_saved_comments() and comment.author != r.user.me():

        #     print ("string found in comment " + comment.id)

        #     comment.reply(random.choice(comment_reply))

        #     print("replied to comment " + comment.id)

        #     comments_replied_to.append(comment.id)

        #     with open('comments_replied_to.txt', 'a') as f:
        #         f.write(comment.id + '\n')

        # if "Jon" in comment.body and comment.id not in get_saved_comments() and comment.author != r.user.me():

        #     print ("string found in comment " + comment.id)

        #     comment.reply(random.choice(comment_reply))

        #     print("replied to comment " + comment.id)

        #     comments_replied_to.append(comment.id)

        #     with open('comments_replied_to.txt', 'a') as f:
        #         f.write(comment.id + '\n')

        # if "jon" in comment.body and comment.id not in get_saved_comments() and comment.author != r.user.me():

        #     print ("string found in comment " + comment.id)

        #     comment.reply(random.choice(comment_reply))

        #     print("replied to comment " + comment.id)

        #     comments_replied_to.append(comment.id)

        #     with open('comments_replied_to.txt', 'a') as f:
        #         f.write(comment.id + '\n')

        # if "Jonathan" in comment.body and comment.id not in get_saved_comments() and comment.author != r.user.me():

        #     print ("string found in comment " + comment.id)

        #     comment.reply(random.choice(comment_reply))

        #     print("replied to comment " + comment.id)

        #     comments_replied_to.append(comment.id)

            #with open('comments_replied_to.txt', 'a') as f:
             #   f.write(comment.id + '\n')

        # if comment.author == 'thom-yorke-bot' and comment.author != r.user.me():
        #     print('Thombot detected')
        #     comment.reply(random.choice(thombot_reply))

        #     print("replied to thombot comment " + comment.id)
        #     comments_replied_to.append(comment.id)

        #     with open('comments_replied_to.txt', 'a') as f:
        #         f.write(comment.id + '\n')


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
