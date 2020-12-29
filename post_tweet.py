import os
from twitter_bot_class import TwitterBot

if __name__ == "__main__":
    try:
        pj = TwitterBot("Mahmoud96118166", '01cd01e1')
        pj.login()
        pj.post_tweets("My bot's first tweet!")
        pj.logout()
    except Exception as e:
        pj.logout()
        print(e)

