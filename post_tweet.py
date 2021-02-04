import os
from twitter_bot_class import TwitterBot
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    try:
        pj = TwitterBot(os.environ['EMAIL'], os.environ['PASSWORD'])
        pj.login()
        pj.post_tweets("Olá São Paulo!")
        pj.logout()
    except Exception as e:
        pj.logout()
        print(e)

