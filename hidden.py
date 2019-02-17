# Keep this file separate

# https://apps.twitter.com/
# Create new App and get the four strings

def oauth():
    consumer_key_i = input("Type or paste your consumer key: ")
    consumer_secret_i = input("Type or paste your consumer secret key: ")
    token_key_i = input("Type or paste your token key: ")
    token_secret_i = input("Type or paste your token secret key: ")
    return {"consumer_key": consumer_key_i,
                "consumer_secret": consumer_secret_i,
                "token_key": token_key_i,
                "token_secret": token_secret_i}