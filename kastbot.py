import os
import time
from slackclient import SlackClient

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

#variables kast bot&
kast_url = "http://signature.rocketleaguestats.com/normal/steam/76561197984517179.png"
nakt_url = "http://signature.rocketleaguestats.com/normal/steam/76561197983296969.png"
samo_url = "http://signature.rocketleaguestats.com/normal/steam/76561197994818514.png"
ragna_url = "http://signature.rocketleaguestats.com/normal/steam/76561197999848401.png"
ryuken_url = "http://signature.rocketleaguestats.com/normal/steam/76561197960366993.png"
john5_url= "http://signature.rocketleaguestats.com/normal/steam/76561197961062191.png"

def handle_command(command, channel):
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."

    if command == "kast rank":
        slack_client.api_call("chat.postMessage", channel=channel, text=kast_url, as_user=True)

    elif command == "nakt rank":
        slack_client.api_call("chat.postMessage", channel=channel, text=nakt_url, as_user=True)

    elif command == "samo rank":
        slack_client.api_call("chat.postMessage", channel=channel, text=samo_url, as_user=True)

    elif command == "ragna rank":
        slack_client.api_call("chat.postMessage", channel=channel, text=ragna_url, as_user=True)

    elif command == "ryuken rank":
        slack_client.api_call("chat.postMessage", channel=channel, text=ryuken_url, as_user=True)

    elif command == "john5 rank":
        slack_client.api_call("chat.postMessage", channel=channel, text=john5_url, as_user=True)

    elif command == "patch note":
        slack_client.api_call("chat.postMessage", channel=channel, text=john5_url, as_user=True)
        http://rocketleague.wikia.com/wiki/Patch_Notes

    else:
        slack_client.api_call("chat.postMessage", channel=channel,
            text="commands available : player rank.", as_user=True)



def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
