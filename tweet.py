# The script man.

import twitter
import re, string, sys 

api = twitter.Api(consumer_key='secret',
                           consumer_secret='secret',
                           access_token_key='secret-secret',
                           access_token_secret='secret')

sys.argv[0] = ""
tweet = ' '.join(sys.argv)
status = api.PostUpdate(tweet)
print status.text