import os
import time
import re
import logging
from slackclient import SlackClient

# This is the way the bot authenticates with slack.  To get a token, please
# talk to Anand
SLACK_BOT_TOKEN = "YOU'LL NEED TO ASK FOR A TOKEN!"

echo_on = False

def handle_direct_mention(message, channel):
    # TODO: This bot should probably do something more interesting...
    global echo_on
    if message == "echo on":
        echo_on = True
    elif message == "echo off":
        echo_on = False

def handle_regular_message(message, channel):
    # TODO: This bot should probably do something more interesting...
    if echo_on:
        send_message(message, channel)

################################################################################
#
# HELPER FUNCTIONS PROVIDED FOR CONVENIENCE
#
################################################################################

def send_message(message, channel):
    """
        Helper function that sends a message to a channel.
    """
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=message
    )


################################################################################
#
# YOU DON'T NEED TO MESS WITH STUFF BELOW THIS.  THIS HANDLES CONNECTING TO
# SLACK, GETTING MESSAGES, AND PARSING THEM.
#
################################################################################

# Set up logging
logging.basicConfig()

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN)
# bot's user ID in Slack: value is assigned after the bot starts up
bot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def handle_events(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find one of:
        1.  Bot commands sent directly to the bot.
        2.  Regular messages to a channel so it can do something if it wants to.
    """
    for event in slack_events:
        # We care about events of type message that have no subtype
        # Messages that have subtype are "meta"; they are things like channel
        # join, messages from bots, etc.  We care about working with regular
        # messages only.
        if event["type"] == "message" and not "subtype" in event:

            # Try parsing the message to see if it was a mention.
            # If it was, and to this bot, then we want to handle the direct
            # mention.
            user_id, message = parse_direct_mention(event["text"])
            if user_id == bot_id:
                # It was a mention to this bot!
                handle_direct_mention(message, event["channel"])
            elif user_id:
                # Do nothing if this was a mention message to something/one else
                pass
            else:
                # This was a regular message.  If we want to do something with
                # it, we can.
                handle_regular_message(event["text"], event["channel"])

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

if __name__ == "__main__":

    # Try connecting to slack!
    if slack_client.rtm_connect(with_team_state=False):
        print("Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        bot_id = slack_client.api_call("auth.test")["user_id"]
        while True:

            # Handle any events that slack has seen
            handle_events(slack_client.rtm_read())

            # Wait some time before trying to read more events
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
