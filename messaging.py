import requests
import os

try:
    BOT_ID = os.environ['BOT_ID']
    TEST_BOT_ID = os.environ['TEST_BOT_ID']
except KeyError:
    print("Could not find environment variable BOT_ID or TEST_BOT_ID")
    BOT_ID = ''
    TEST_BOT_ID = ''
#FIXME: comment this to go back to production
#BOT_ID = TEST_BOT_ID


def send_message(text):
	if len(text) > 1000:
		text = text[:1000]
	print("sending: {}".format(text))
	requests.post("https://api.groupme.com/v3/bots/post", data={
		"bot_id"  : BOT_ID,
		"text"    : text
	})

# liking is not supported by bots in groupme
'''
def like_message(conversation_id, message_id):
	print("liking a message")
	requests.post("https://api.groupme.com/v3/messages/:{}/:{}/like?token={}".format(conversation_id, message_id, BOT_ID))
'''
